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
Requires:       python >= 2.7

%define userid root

BuildArch: %{arch}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/%{_rootdir}/bin
mkdir -p %{buildroot}/%{_rootdir}/examples
mkdir -p %{buildroot}/%{_rootdir}/bin/docopt
mkdir -p %{buildroot}/%{_rootdir}/bin/gosec_filter
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/gsf %{buildroot}/%{_rootdir}/bin
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/docopt/__init__.py %{buildroot}/%{_rootdir}/bin/docopt
install -p -m 755 %{_builddir}/%{name}-%{version}/bin/gosec_filter/__init__.py %{buildroot}/%{_rootdir}/bin/gosec_filter
install -p -m 755 %{_builddir}/%{name}-%{version}/examples/statsbe_filter.py %{buildroot}/%{_rootdir}/examples
install -p -m 755 %{_builddir}/%{name}-%{version}/examples/gosec_report.txt %{buildroot}/%{_rootdir}/examples

%description
Filter gosec reports (see https://github.com/securego/gosec) when output in txt mode

%files
%{_rootdir}/bin/gsf
%{_rootdir}/bin/docopt/__init__.py
%{_rootdir}/bin/gosec_filter/__init__.py
%{_rootdir}/examples/statsbe_filter.py
%{_rootdir}/examples/gosec_report.txt

%post
# HACK: beego needs conf directory lives in the same dir as app executable
chmod +x /opt/gsf/bin/gsf
cd /usr/bin; [ -s gsf ] || ln -s /opt/gsf/bin/gsf

echo ""
echo "GSF has been installed in %{_rootdir}"
echo ""
