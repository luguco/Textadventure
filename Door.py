class Door(object):
    def __init__(self, pstatus, pdirection, ppos):
        self.status = pstatus
        self.direction = pdirection
        self.position = ppos

    def getStatus(self):
        return self.status

    def getDirection(self):
        return self.direction

    def getPosition(self):
        return self.position

    def open(self):
        if not self.status == 'broken':
            self.status = "open"

    def close(self):
        self.status = "close"

