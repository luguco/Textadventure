class Object(object):
    def __init__(self, pname, pid, pmovable, pinv):
        self.name = pname
        self.id = pid
        self.movable = pmovable
        self.inventory = pinv

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def isMovable(self):
        return self.movable

    def getInventory(self):
        return self.inventory

    def setInventory(self, pinv):
        self.inventory = pinv

