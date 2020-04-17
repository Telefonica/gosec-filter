APP       := gsf
VERSION   ?= $(shell git describe --abbrev=0 --tags)
RELEASE   ?= $(shell git rev-parse --short HEAD)
TOP       := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BRANCH    ?= master
EXTENSION := $(shell echo ${BRANCH} | tr "/" "_")
ARCH      := x86_64
TMP       := $(TOP)/tmp

.PHONY: sdist \
	install \
	uninstall \
	rpm \
	deb \
	upprof \
	upblock \
	clean

define helptxt

gsf is GoSec Filter

usage: make <command>

commands:
	sdist      - Creates a .tgz distribution of the package
	install    - Installs without packaging
	uninstall  - Uninstalls without updating packaging DBs
	rpm        - Creates rpm package
	deb        - Creates deb package
	clean      - Removes generated files and directories
	upprof     - update profile-be filter with non filtered definitions in /tmp/gosec_report.txt
	upblock    - update blocking filter with non filtered definitions in /tmp/gosec_report.txt

endef
export helptxt

all: help

help:
	@echo "$$helptxt"

sdist: 
	$(info) "Creating source distribution..."
	mkdir -p $(TOP)/dist/$(APP)-$(VERSION)/bin
	mkdir -p $(TOP)/dist/$(APP)-$(VERSION)/examples
	cp -a $(TOP)/cmd/* $(TOP)/dist/$(APP)-$(VERSION)/bin
	cp -a $(TOP)/examples/* $(TOP)/dist/$(APP)-$(VERSION)/examples
	cd $(TOP)/dist; tar zcf $(APP)-$(VERSION).tgz $(APP)-$(VERSION)/*
	@echo

install:
	$(info) "Installing without packaging..."
	mkdir -p /opt
	mkdir /opt/$(APP)
	mkdir -p /opt/$(APP)/bin
	mkdir -p /opt/$(APP)/examples
	cp -a $(TOP)/cmd/* /opt/$(APP)/bin
	cp -a $(TOP)/examples/* /opt/$(APP)/examples
	chmod +x /opt/$(APP)/bin/$(APP)
	cd /usr/bin; [ -s gsf ] || ln -s /opt/gsf/bin/gsf
	cd /usr/bin; [ -s gen_amdocs_filter ] || ln -s /opt/gsf/bin/gen_amdocs_filter
	cd /usr/bin; [ -s gen_blocking_filter ] || ln -s /opt/gsf/bin/gen_blocking_filter
	cd /usr/bin; [ -s gen_devices_filter ] || ln -s /opt/gsf/bin/gen_devices_filter
	cd /usr/bin; [ -s gen_profbe_filter ] || ln -s /opt/gsf/bin/gen_profbe_filter
	cd /usr/bin; [ -s gen_stats_filter ] || ln -s /opt/gsf/bin/gen_stats_filter

	$(info) "done"

uninstall:
	$(info) "Installing without packaging..."
	cd /opt/$(APP) && rm -Rf bin && rm -Rf examples
	cd /opt &&	rmdir $(APP)
	cd / &&	rmdir opt || true
	rm -f /usr/bin/gsf
	$(info) "done"

rpm: sdist
	$(info) "Creating rpm packages..."
	mkdir -p $(TMP)/rpmbuild/RPMS
	mkdir -p $(TMP)/rpmbuild/BUILD
	mkdir -p $(TMP)/rpmbuild/SOURCES
	cp $(TOP)/dist/$(APP)-$(VERSION).tgz $(TMP)/rpmbuild/SOURCES
	rpmbuild -bb $(TOP)/$(APP).spec                          \
			 --define "extension $(EXTENSION)"               \
			 --define "version $(VERSION)"                   \
			 --define "release $(RELEASE)"                   \
			 --define "arch $(ARCH)"                         \
			 --define "_target_os linux"                     \
			 --define "_topdir $(TMP)/rpmbuild"              \
			 --define "buildroot $(TMP)/rpmbuild/BUILDROOT"  \
			 --define "_rootdir /opt/gsf"                    \
			 --buildroot=$(TMP)/rpmbuild/BUILDROOT
	mv $(TMP)/rpmbuild/RPMS/$(ARCH)/$(APP)-$(VERSION)-$(RELEASE).$(ARCH).rpm $(TOP)
	@echo
	$(info) "Created packages in $(TOP)/$(APP)-$(VERSION)-$(RELEASE).$(ARCH).rpm"
	@echo

deb: rpm
	@fakeroot alien $(TOP)/$(APP)-$(VERSION)-$(RELEASE).$(ARCH).rpm --scripts

clean:
	rm -rf dist/
	rm -rf tmp/
	rm -f *.rpm
	rm -f *.deb

upprof:
	gen_profbe_filter /tmp/gosec_report.txt > $(TOP)/examples/profbe_filter.py

upblock:
	gen_blocking_filter /tmp/gosec_report.txt > $(TOP)/examples/blocking_filter.py

info := @printf "\033[32;01m >>> %s\033[0m\n"
