
from gosec_filter import StatsbeGosecWarning
fileSplitRoot = StatsbeGosecWarning.fileSplitRoot

the_gosec_filter = set([ 
StatsbeGosecWarning(error='G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:28',
             code='DM_PARENTAL_CHILD_RULE_TOKEN    = `policy_niji_child`'), 
StatsbeGosecWarning(error='G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:30',
             code='DM_MALWARE_RULE_TOKEN           = `policy_niji_malware`'), 
StatsbeGosecWarning(error='G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:31',
             code='DM_PHISHING_SKIP_RULE_TOKEN     = `phishing allow user`'), 
StatsbeGosecWarning(error='G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:35',
             code='DM_PHISHING_RULE_WEB_WL_TOKEN   = `AntiPhishWebWL`'), 
StatsbeGosecWarning(error='G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/dm.go:36',
             code='DM_PHISHING_RULE_MAIN_WL_TOKEN  = `AntiPhishMailWL`'), 
StatsbeGosecWarning(error='G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/parser-commons.go:269',
             code='os.Open(filename)'), 
StatsbeGosecWarning(error='G304: Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)',
             location='/home/mlg/go/src/niji-statistics/src/awazza-statistic-be/parser/statefulparser.go:129',
             code='os.Open(logFilePath)'), 
])

