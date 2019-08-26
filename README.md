# GSF is GoSec Filter
This is a filter for gosec (https://github.com/securego/gosec) reports

**Requires python 2.7 or higher to be executed and rpmbuild to be built.**

## On CentOS or Red Hat platforms:
### To build package: 
    make rpm
### To install:
    sudo rpm -i gsf-version-release.rpm
### To uninstall:
    sudo rpm -e gsf-version-release.rpm

## On Debian platforms:
**Requires alien to build .deb file**
### To build package:
    make deb
### To install:
    sudo dpkg -i gsf-version-release.deb
### To uninstall:
    sudo dpkg --remove gsf


