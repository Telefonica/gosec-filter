from gosec_filter import GosecWarning

the_gosec_filter = set([\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)",\
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/dm.go:27",\
             code="DM_PARENTAL_CHILD_RULE_TOKEN    = `policy_niji_child`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)",
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/dm.go:29",\
             code="DM_MALWARE_RULE_TOKEN           = `policy_niji_malware`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", 
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/dm.go:30",\
             code="DM_PHISHING_SKIP_RULE_TOKEN     = `phishing allow user`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", 
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/dm.go:34",\
             code="DM_PHISHING_RULE_WEB_WL_TOKEN   = `AntiPhishWebWL`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", 
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/dm.go:35",\
             code="DM_PHISHING_RULE_MAIN_WL_TOKEN  = `AntiPhishMailWL`"),\
GosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)",
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/parser-commons.go:260",\
             code="os.Open(filename)"),\
GosecWarning(error="G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)", 
             location="/home/contint/go/src/github.com/Telefonica/niji-statistics/src/awazza-statistic-be/parser/statefulparser.go:129",\
             code="os.Open(logFilePath)"),\
])
