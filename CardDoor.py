from Door import *


class CardDoor(Door):
    def __init__(self, plevel):
        self.level = plevel
        self.status = "close"

    def open(self, plevel):
        if plevel >= self.level:
            self.status = "open"
            return True
        return False
