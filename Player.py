class Player(object):
    def __init__(self, pname, pfacing, pinv, ppos):
        self.name = pname
        self.facing = pfacing
        self.inventory = pinv
        self.position = ppos

    def getName(self):
        return self.name

    def setName(self, pname):
        self.name = pname

    def getInventory(self):
        return self.inventory

    def setInventory(self, pinv):
        self.inventory = pinv

    def getFacing(self):
        return self.facing

    def setFacing(self, pfacing):
        self.facing = pfacing

    def getPosition(self):
        return self.position

    def setPosition(self, ppos):
        self.position = ppos