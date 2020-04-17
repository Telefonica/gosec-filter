def compareGoProjectFiles(a, b, root):
    aa = str.split(a, root)
    bb = str.split(b, root)
    if len(aa) != 2:
        #print "COMPARE is False 1"
        return False
    elif len(bb) != 2:   
        #print "COMPARE is False 2"
        return False

    #print "COMPARE is " + str(a[1] == bb[1])
    return aa[1] == bb[1]

def getRootPart(a, root):
    aa = str.split(a, root)
    if len(aa) != 2:
        #print "GETROOT(%s, %s) == %s" % (a, root, a) 
        return a
    #print "GETROOT(%s, %s) == %s" % (a, root, aa[1]) 
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
            #print "LOCATION "+location
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
        h = hash(getRootPart(self.lfile, self.fileSplitRoot)+str(self.line)+self.error+self.code)
        #print "HASH of lfile(%s) is done on %s == %d" % (self.lfile, getRootPart(self.lfile, self.fileSplitRoot)+self.error+self.code, h)
        return h

class ProfbeGosecWarning(GosecWarning):
    fileSplitRoot = "/niji-profile/src/"
    def __init__(self, location="", error="", code="", store=False):
        GosecWarning.__init__(self, location, error, code, store, ProfbeGosecWarning.fileSplitRoot)

class StatsbeGosecWarning(GosecWarning):
    fileSplitRoot = "/niji-statistics/src/"
    def __init__(self, location="", error="", code="", store=False):
        GosecWarning.__init__(self, location, error, code, store, StatsbeGosecWarning.fileSplitRoot)

class AmdocsGosecWarning(GosecWarning):
    fileSplitRoot =  "/niji-amdocsadapter/src/"
    def __init__(self, location="", error="", code="", store=False):
        GosecWarning.__init__(self, location, error, code, store, AmdocsGosecWarning.fileSplitRoot)

class DevicesGosecWarning(GosecWarning):
    fileSplitRoot = "/niji-mcafee/avdevice/"
    def __init__(self, location="", error="", code="", store=False):
        GosecWarning.__init__(self, location, error, code, store, DevicesGosecWarning.fileSplitRoot)

class BlockingGosecWarning(GosecWarning):
    fileSplitRoot = "/niji-blocking/src/"
    def __init__(self, location="", error="", code="", store=False):
        GosecWarning.__init__(self, location, error, code, store, BlockingGosecWarning.fileSplitRoot)

