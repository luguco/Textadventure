# TODO: ADD DOORNAME
class Door(object):
    def __init__(self, pstatus, ppos, pname):
        self.status = pstatus
        self.position = ppos
        self.name = pname

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def getPosition(self):
        return self.position

    def open(self):
        if not self.status == 'broken':
            self.status = "open"

    def close(self):
        self.status = "close"

