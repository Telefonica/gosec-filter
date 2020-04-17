from gosec_filter import BlockingGosecWarning

fileSplitRoot = BlockingGosecWarning.fileSplitRoot

the_gosec_filter = set([\
BlockingGosecWarning(error="G505: Blacklisted import crypto/sha1: weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",\
             location="/home/contint/go/src/github.com/Telefonica/niji-blocking/src/niji-blocking/blocking.go:10",\
             code='"crypto/sha1"'),\
BlockingGosecWarning(error="G401: Use of weak cryptographic primitive (Confidence: HIGH, Severity: MEDIUM)",\
             location="/home/contint/go/src/github.com/Telefonica/niji-blocking/src/niji-blocking/blocking.go:182",\
             code="md5.New()"),\
BlockingGosecWarning(error="G107: Potential HTTP request made with variable url (Confidence: MEDIUM, Severity: MEDIUM)",\
             location="/home/contint/go/src/github.com/Telefonica/niji-blocking/src/niji-blocking/cmd/templater/main.go:31",\
             code="http.Get(sheetURL)"),\
])
