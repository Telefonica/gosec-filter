
from gosec_filter import DevicesGosecWarning

fileSplitRoot = DevicesGosecWarning.fileSplitRoot

the_gosec_filter = set([ 
DevicesGosecWarning(error='G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)',
             location='/home/mlg/go/src/niji-mcafee/avdevice/alarms.go:36',
             code='AlarmTokenCallback Alarm = "MCAFEE_TOKEN_02"'), 
DevicesGosecWarning(error='G505: Blacklisted import crypto/sha1: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)',
             location='/home/mlg/go/src/niji-mcafee/avdevice/token.go:6',
             code='"crypto/sha1"'), 
])

