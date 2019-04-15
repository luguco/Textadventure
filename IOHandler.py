class IOHandler(object):
    def __init__(self, pgametype):
        self.gametype = pgametype

    def getInput(self, msg: str) -> str:
        if self.gametype == "console":
            return input(msg)

    def setOutput(self, msg: str):
        if self.gametype == "console":
            print(msg)