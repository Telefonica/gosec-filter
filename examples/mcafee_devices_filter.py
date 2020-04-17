from gosec_filter import DevicesGosecWarning

fileSplitRoot = DevicesGosecWarning.fileSplitRoot

the_gosec_filter = set([\
DevicesGosecWarning(location="/home/contint/go/src/github.com/Telefonica/niji-mcafee/avdevice/token.go:6",\
             error="G505: Blacklisted import crypto/sha1: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",\
             code='"crypto/sha1"'),\
])
