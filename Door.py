# TODO: ADD DOORNAME
class Door(object):
    def __init__(self, pstatus, ppos, pname):
        self.status = pstatus
        self.position = ppos
        self.name = pname

    def getName(self)-> str:
        return self.name

    def getStatus(self)-> str:
        return self.status

    def getPosition(self)-> list:
        return self.position

    def open(self)-> None:
        if not self.status == 'broken':
            self.status = "open"

    def close(self)-> None:
        self.status = "close"

