# GSF is GoSec Filter
This is a filter for gosec (https://github.com/securego/gosec) reports.

    $ gsf
    Usage:
        gosec-filter [-h|--help] <report> <filter>
    
    Options:
        -h --help     Show this screen.
    Details:
        report      the path to the GOSEC report in txt format
        filter      the path to the filter python module

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

## Filtering example

    $ gsf /opt/gsf/examples/gosec_report.txt /opt/gsf/examples/statsbe_filter.py
    opening /opt/gsf/examples/gosec_report.txt
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:35
    What : G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)
    Code : DM_PHISHING_RULE_MAIN_WL_TOKEN  = `AntiPhishMailWL`
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:34
    What : G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)
    Code : DM_PHISHING_RULE_WEB_WL_TOKEN   = `AntiPhishWebWL`
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:30
    What : G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)
    Code : DM_PHISHING_SKIP_RULE_TOKEN     = `phishing allow user`
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:29
    What : G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)
    Code : DM_MALWARE_RULE_TOKEN           = `policy_niji_malware`
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/statefulparser.go:129
    What : G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)
    Code : os.Open(logFilePath)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/parser-commons.go:260
    What : G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)
    Code : os.Open(filename)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/cmd/mcafee-parser/mcafee-parser.go:59
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : os.Stderr.WriteString(logline + "\n")
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:356
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : m.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:364
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : m.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:373
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : m.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/cmd/curl-global-mw-daily-stats/curl-global-mw-daily-stats.go:35
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : w.WriteString(st)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/cmd/curl-global-mw-daily-stats/curl-global-mw-daily-stats.go:132
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : w.WriteString("Date,VirusName,Name,Type,Amount\n")
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/cmd/curl-global-mw-daily-stats/curl-global-mw-daily-stats.go:174
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : w.Flush()
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/cmd/curl-global-mw-daily-stats/curl-global-mw-daily-stats.go:182
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : e.AttachFile(outputFileName)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:346
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : m.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:338
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : m.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:288
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : conn_p.Close()
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/queuemgr.go:284
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : ch_p.Close()
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/janitor.go:300
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : saveCleanInfo(janitorUser)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/janitor.go:253
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : key.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/janitor/janitor.go:248
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : key.Ack(false)
    
    Where: /home/mlg/go/src/niji-statistics/src/awazza-statistic-be/cmd/awazza-st-be/awazza-st-be.go:82
    What : G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
    Code : pprof.StartCPUProfile(f)
    
    1 filtered security warning(s) of 23 warning(s)


