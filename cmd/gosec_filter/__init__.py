class GosecWarning:
    store = False
    location = ""
    error    = ""
    code     = ""
    def __init__(self, location="", error="", code="", store=False):
        self.location = location
        self.error    = error
        self.code     = code
        self.store    = store
    def __str__(self):
        return "Where: %s\nWhat : %s\nCode : %s\n" % (self.location, self.error, self.code)
    def __eq__(self, other):
        #Note: we dont filter by location
        return self.error == other.error and self.code == other.code
    def __hash__(self):
        #Note: we dont filter by location        
        #h = hash(self.error+self.code)
        #print "hash of \""+self.error+self.code+"\" is "+str(h)
        return hash(self.error+self.code)
