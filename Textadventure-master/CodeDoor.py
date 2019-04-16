from Door import *


class CodeDoor(Door):
    def __init__(self, pstatus, pdirection, ppos, pcode):
        self.code = pcode
        self.status = pstatus
        self.direction = pdirection
        self.position = ppos

    def open(self, pcode):
        if pcode == self.code:
            self.status = "open"
            return True
        return False
