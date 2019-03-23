class Door(object):
    def __int__(self):
        self.status = "close"

    def getStatus(self):
        return self.status

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "close"
