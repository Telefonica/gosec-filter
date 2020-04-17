def compareGoProjectFiles(a, b, root):
    aa = str.split(a, root)
    bb = str.split(b, root)
    if len(aa) != 2:
        return False
    elif len(bb) != 2:   
        return False

    return aa[1] == bb[1]

def getRootPart(a, root):
    aa = str.split(a, root)
    if len(aa) != 2:
        return aa
    return aa[1]

class GosecWarning:
    fileSplitRoot = ""
    location = ""
    lfile    = ""
    line     = ""
    error    = ""
    code     = ""
    store    = False
    def __init__(self, location="", error="", code="", store=False, fileSplitRoot=""):
        if location != "" :
            self.location = location
            self.fileSplitRoot = fileSplitRoot
            tmp = location.split(":")
            if len(tmp) != 2 :
                raise Exception("invalid len for location split (%d) location(%s)", len(tmp), location)
            self.lfile    = tmp[0]
            self.line     = tmp[1]
        self.error    = error
        self.code     = code
        self.store    = store
    def __str__(self):
        return "Where: %s\nWhat : %s\nCode : %s\n" % (self.lfile+":"+self.line, self.error, self.code)
    def __eq__(self, other):
        #Note: we dont filter by location
        if self.fileSplitRoot != "":
            ret = compareGoProjectFiles(self.lfile, other.lfile, self.fileSplitRoot) and self.line == other.line and self.error == other.error and self.code == other.code
            #print compareGoProjectFiles(self.lfile, other.lfile, self.fileSplitRoot)
        else:
            ret = compareGoProjectFiles(self.lfile, other.lfile, "/go/src/") and self.line == other.line and self.error == other.error and self.code == other.code
            #print compareGoProjectFiles(self.lfile, other.lfile, "/go/src/")

        #print "fspr..." +  self.fileSplitRoot
        #print "self..." + self.lfile
        #print "other.." + other.lfile

        return ret

    def __hash__(self):
        #Note: we dont filter by whole location, just file, may have false positives, control number of filter hits vs filter definitions.
        #h = hash(self.error+self.code)
        #print "hash of \""+self.error+self.code+"\" is "+str(h)
        return hash(getRootPart(self.lfile, self.fileSplitRoot)+self.error+self.code)

class ProfbeGosecWarning(GosecWarning):
    def __init__(self, location="", error="", code="", store=False):
        GosecWarning.__init__(self, location, error, code, store, "/niji-profile/src/")

