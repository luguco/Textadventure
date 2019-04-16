from Door import *


class CardDoor(Door):
    def __init__(self, pstatus, pdirection, ppos, plevel):
        self.level = plevel
        self.status = pstatus
        self.direction = pdirection
        self.position = ppos

    def open(self, plevel):
        if plevel >= self.level:
            self.status = "open"
            return True
        return False
