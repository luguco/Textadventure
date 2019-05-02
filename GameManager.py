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
        # p = self.mapmanager.getPlayer()
        # iohandler.setOutput(msghandler.getMessage("introduction-welcome"))
        # name = iohandler.getInput(msghandler.getMessage("introduction-name"))
        # p.setName(name)
        # iohandler.setOutput(msghandler.getMessage("introduction-personalwelcome").replace("%name%", p.getName()))
        # iohandler.setOutput(msghandler.getMessage("introduction-help"))
        # res = iohandler.getInput(msghandler.getMessage("introduction-helpcommands"))
        #
        # while res != "help commands":
        #     res = iohandler.getInput(msghandler.getMessage("general-invalidintroductionhelpcommand"))
        #
        # iohandler.setOutput(msghandler.getMessage("general-seperator"))
        # iohandler.setOutput(msghandler.getMessage("commands-commands-info"))
        # iohandler.setOutput(msghandler.getMessage("introduction-end"))

        # Game begin
        while True:
            iohandler.setOutput(msghandler.getMessage("general-seperator"))
            input = self.iohandler.getInput(msghandler.getMessage("general-input"))
            self.__handleCommand(input)

# TODO: INVENTORY HANDLE COMMANDS
# TODO: GET FACING COMMANDS
# TODO: GET COORDINATES
# TODO: INTERACT WITH OBJECTS

    def __handleCommand(self, input: str):
        msghandler = self.messagehandler
        iohandler = self.iohandler

        rawcommand = input.split(" ")
        command = rawcommand[0]
        args = rawcommand[1:]

        if command == "help" and len(args) == 1:
            iohandler.setOutput(msghandler.getMessage("commands-" + args[0] + "-info"))

        elif command == "quit":
            # TODO: FINAL QUESTION FOR EXIT
            exit(0)

        elif command == "commands":
            iohandler.setOutput(msghandler.getMessage("commands-commands"))

        elif command == "left":
            self.mapmanager.rotatePlayer("left")
            direction = msghandler.getMessage("turn-left")
            facing = msghandler.getMessage("turn-" + self.mapmanager.getPlayer().getFacing())
            msg = msghandler.getMessage("turn-general").replace("%direction%", direction).replace("%facing%", facing)
            iohandler.setOutput(msg)

        elif command == "right":
            self.mapmanager.rotatePlayer("right")
            direction = msghandler.getMessage("turn-right")
            facing = msghandler.getMessage("turn-" + self.mapmanager.getPlayer().getFacing())
            msg = msghandler.getMessage("turn-general").replace("%direction%", direction).replace("%facing%", facing)
            iohandler.setOutput(msg)

        elif command == "lookaround":
            objects = self.mapmanager.getVisibleObjects()
            for o in objects:
                direction = o[2]
                objtype = o[0]
                msg = ""

                # left
                if direction == 0:
                    if objtype == "wall":
                        msg = msghandler.getMessage("lookaround-left").replace("%object%", msghandler.getMessage("lookaround-wall"))

                    elif objtype == "door":
                        msg = msghandler.getMessage("lookaround-left").replace("%object%", msghandler.getMessage("lookaround-door"))
                        msg = msg + "\n" + msghandler.getMessage("lookaround-doorname").replace("%doorname%", o[1].getName())

                    elif objtype == "object":
                        msg = msghandler.getMessage("lookaround-left").replace("%object%", o[1].getName())
                # front
                elif direction == 1:
                    if objtype == "wall":
                        msg = msghandler.getMessage("lookaround-front").replace("%object%", msghandler.getMessage("lookaround-wall"))

                    elif objtype == "door":
                        msg = msghandler.getMessage("lookaround-front").replace("%object%", msghandler.getMessage("lookaround-door"))
                        msg = msg + "\n" + msghandler.getMessage("lookaround-doorname").replace("%doorname%",
                                                                                                o[1].getName())

                    elif objtype == "object":
                        msg = msghandler.getMessage("lookaround-front").replace("%object%", o[1].getName())

                # right
                elif direction == 2:
                    if objtype == "wall":
                        msg = msghandler.getMessage("lookaround-right").replace("%object%", msghandler.getMessage("lookaround-wall"))

                    elif objtype == "door":
                        msg = msghandler.getMessage("lookaround-right").replace("%object%",msghandler.getMessage("lookaround-door"))
                        msg = msg + "\n" + msghandler.getMessage("lookaround-doorname").replace("%doorname%", o[1].getName())

                    elif objtype == "object":
                        msg = msghandler.getMessage("lookaround-right").replace("%object%", o[1].getName())
                if len(msg) > 0:
                    iohandler.setOutput(msg)

        else:
            iohandler.setOutput(msghandler.getMessage("general-invalidcommand"))


g = GameManager()
g.start()