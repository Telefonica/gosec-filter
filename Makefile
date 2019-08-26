APP       := gsf
VERSION   ?= $(shell git describe --abbrev=0 --tags)
RELEASE   ?= $(shell git rev-parse --short HEAD)
TOP       := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BRANCH    ?= master
EXTENSION := $(shell echo ${BRANCH} | tr "/" "_")
ARCH      := x86_64
TMP       := $(TOP)/tmp


sdist: 
	$(info) "Creating source distribution..."
	mkdir -p $(TOP)/dist/$(APP)-$(VERSION)/bin
	cp -a $(TOP)/cmd/* $(TOP)/dist/$(APP)-$(VERSION)/bin
	cd $(TOP)/dist; tar zcf $(APP)-$(VERSION).tgz $(APP)-$(VERSION)/*
	@echo

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
	rm *.rpm
	rm *.deb

info := @printf "\033[32;01m >>> %s\033[0m\n"
