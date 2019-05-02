from Door import *


class CardDoor(Door):
    def __init__(self, pstatus, ppos, plevel, pname):
        self.level = plevel
        self.status = pstatus
        self.position = ppos
        self.name = pname

    def open(self, plevel):
        if plevel >= self.level:
            self.status = "open"
            return True
        return False
