class GosecWarning:
    lfile    = ""
    line     = ""
    error    = ""
    code     = ""
    store    = False
    def __init__(self, location="", error="", code="", store=False):
        tmp = location.split(":")
        self.lfile    = tmp[0]
        self.line     = tmp[1]
        self.error    = error
        self.code     = code
        self.store    = store
    def __str__(self):
        return "Where: %s\nWhat : %s\nCode : %s\n" % (self.lfile+":"+self.line, self.error, self.code)
    def __eq__(self, other):
        #Note: we dont filter by location
        return self.lfile == other.lfile and self.line == other.line and self.error == other.error and self.code == other.code
    def __hash__(self):
        #Note: we dont filter by whole location, just file, may have false positives, control number of filter hits vs filter definitions.
        #h = hash(self.error+self.code)
        #print "hash of \""+self.error+self.code+"\" is "+str(h)
        return hash(self.lfile+self.error+self.code)
