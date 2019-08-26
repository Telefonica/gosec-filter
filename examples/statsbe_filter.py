from gosec_filter import GosecWarning

the_gosec_filter = set([\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", code="DM_PARENTAL_CHILD_RULE_TOKEN    = `policy_niji_child`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", code="DM_MALWARE_RULE_TOKEN           = `policy_niji_malware`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", code="DM_PHISHING_SKIP_RULE_TOKEN     = `phishing allow user`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", code="DM_PHISHING_RULE_WEB_WL_TOKEN   = `AntiPhishWebWL`"),\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", code="DM_PHISHING_RULE_MAIN_WL_TOKEN  = `AntiPhishMailWL"),\
])
