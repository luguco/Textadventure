class IOHandler(object):
    def __init__(self, pgametype, pgui):
        self.gametype = pgametype
        self.gui = pgui

    def getInput(self, msg: str) -> str:
        if self.gametype == "console":
            return input(msg)
        else:
            e = self.gui.textentry
            i = e.get("1.0", "end-1c")
            return i

    def setOutput(self, msg: str):
        if self.gametype == "console":
            print(msg)
        else:
            if len(msg) > 0:
                self.gui.write(msg + "\n-------------------------------------------------------------------------------------------\n")
