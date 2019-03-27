class Object(object):
    def __init__(self, pname, pid, pmovable, ppickable, pinv):
        self.name = pname
        self.id = pid
        self.movable = pmovable
        self.inventory = pinv
        self.pickable = ppickable

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def isMovable(self):
        return self.movable

    def isPickable(self):
        return self.pickable

    def getInventory(self):
        return self.inventory

    def setInventory(self, pinv):
        self.inventory = pinv

