from Door import *


class CodeDoor(Door):
    def __init__(self, pcode):
        self.code = pcode
        self.status = "close"

    def open(self, pcode):
        if pcode == self.code:
            self.status = "open"
            return True
        return False
