class Person(object):
    def __init__(self, pname, ptype, pfacing, ppos):
        self.name = pname
        self.type = ptype
        self.facing = pfacing
        self.position = ppos

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getFacing(self):
        return self.facing

    def getPosition(self):
        return self.position