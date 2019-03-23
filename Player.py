class Player(object):
    def __init__(self, pname, pfacing, pinv):
        self.name = pname
        self.facing = pfacing
        self.inventory = pinv

    def getName(self):
        return self.name

    def getInventory(self):
        return self.inventory

    def setInventory(self, pinv):
        self.inventory = pinv

    def getFacing(self):
        return self.facing

    def setFacing(self, pfacing):
        self.facing = pfacing
