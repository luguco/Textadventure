from Door import *


class CodeDoor(Door):
    def __init__(self, pstatus, ppos, pcode, pname):
        self.code = pcode
        self.status = pstatus
        self.position = ppos
        self.name = pname

    def open(self, pcode):
        if pcode == self.code:
            self.status = "open"
            return True
        return False
