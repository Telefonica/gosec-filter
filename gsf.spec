%global debug_package %{nil}
# Disable strict checks
%global _unpackaged_files_terminate_build  0
%global _missing_doc_files_terminate_build 0

Name:           gsf
Summary:        Gosec Filter
Version:        %{version}
Release:        %{release}
License:        Proprietary
Group:          System Environment/Base
URL:            http://www.telefonica.com
Source0:        %{name}-%{version}.tgz

%define userid root

BuildArch: %{arch}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_rootdir}/bin
mkdir -p %{buildroot}/%{_rootdir}/bin/docopt
mkdir -p %{buildroot}/%{_rootdir}/bin/filters
mkdir -p %{buildroot}/%{_rootdir}/bin/gosec_filter
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/gsf %{buildroot}/%{_rootdir}/bin
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/docopt/__init__.py %{buildroot}/%{_rootdir}/bin/docopt
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/filters/statsbe_filter.py %{buildroot}/%{_rootdir}/bin/filters
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/gosec_filter/__init__.py %{buildroot}/%{_rootdir}/bin/gosec_filter

%description
Filter gosec reports (see https://github.com/securego/gosec) when output in txt mode

%files
%{_rootdir}/bin/gsf
%{_rootdir}/bin/docopt/__init__.py
%{_rootdir}/bin/filters/statsbe_filter.py
%{_rootdir}/bin/gosec_filter/__init__.py

%post
# HACK: beego needs conf directory lives in the same dir as app executable
#cd %{_rootdir}/bin; [ -s conf ] || ln -s ../conf/
cd /usr/bin; [ -s gsf ] || ln -s /opt/gsf/bin/gsf

echo ""
echo "installed in %{_rootdir}/bin"
echo ""
