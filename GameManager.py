from FileSystem import *
from MapManager import *
from IOHandler import *
from MessageHandler import *
from sys import exit


class GameManager(object):
    def __init__(self):
        self.filesystem = FileSystem()
        self.mapmanager = MapManager(self.filesystem.getData('map'))
        self.mapmanager.getVisibleObjects()
        self.iohandler = IOHandler("console")
        self.messagehandler = MessageHandler(self.filesystem.getData("messages"))

    def start(self):
        msghandler = self.messagehandler
        iohandler = self.iohandler

        # Tutorial
        p = self.mapmanager.getPlayer()
        iohandler.setOutput(msghandler.getMessage("introduction-welcome"))
        name = iohandler.getInput(msghandler.getMessage("introduction-name"))
        p.setName(name)
        iohandler.setOutput(msghandler.getMessage("introduction-personalwelcome").replace("%name%", p.getName()))
        iohandler.setOutput(msghandler.getMessage("introduction-help"))
        res = iohandler.getInput(msghandler.getMessage("introduction-helpcommands"))

        while res != "help commands":
            res = iohandler.getInput(msghandler.getMessage("general-invalidintroductionhelpcommand"))

        iohandler.setOutput(msghandler.getMessage("general-seperator"))
        iohandler.setOutput(msghandler.getMessage("commands-commands-info"))
        iohandler.setOutput(msghandler.getMessage("introduction-end"))

        # Game begin
        while True:
            iohandler.setOutput(msghandler.getMessage("general-seperator"))
            input = self.iohandler.getInput(msghandler.getMessage("general-input"))
            self.__handleCommand(input)

    def __handleCommand(self, input: str):
        msghandler = self.messagehandler
        iohandler = self.iohandler

        rawcommand = input.split(" ")
        command = rawcommand[0]
        args = rawcommand[1:]

        if command == "help" and len(args) == 1:
            iohandler.setOutput(msghandler.getMessage("commands-" + args[0] + "-info"))
        elif command == "quit":
            exit(0)
        else:
            iohandler.setOutput(msghandler.getMessage("general-invalidcommand"))



g = GameManager()
g.start()