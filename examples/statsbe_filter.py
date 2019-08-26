from gosec_filter import GosecWarning

the_gosec_filter = set([\
GosecWarning(error="G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)", code="DM_PARENTAL_CHILD_RULE_TOKEN    = `policy_niji_child`")\
])
