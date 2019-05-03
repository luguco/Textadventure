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

# TODO: GOING THROUGH DOORS
# TODO: UPDATE HELP COMMANDS

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
                        msg = msg + "\n" + msghandler.getMessage("lookaround-doorstatus").replace("%status%",  msghandler.getMessage("lookaround-" + o[1].getStatus()))

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
                        msg = msg + "\n" + msghandler.getMessage(
                            "lookaround-doorstatus").replace("%status%", msghandler.getMessage("lookaround-" + o[1].getStatus()))

                    elif objtype == "object":
                        msg = msghandler.getMessage("lookaround-front").replace("%object%", o[1].getName())

                # right
                elif direction == 2:
                    if objtype == "wall":
                        msg = msghandler.getMessage("lookaround-right").replace("%object%", msghandler.getMessage("lookaround-wall"))

                    elif objtype == "door":
                        msg = msghandler.getMessage("lookaround-right").replace("%object%", msghandler.getMessage("lookaround-door"))
                        msg = msg + "\n" + msghandler.getMessage("lookaround-doorname").replace("%doorname%", o[1].getName())
                        msg = msg + "\n" + msghandler.getMessage(
                            "lookaround-doorstatus").replace("%status%",  msghandler.getMessage("lookaround-" + o[1].getStatus()))

                    elif objtype == "object":
                        msg = msghandler.getMessage("lookaround-right").replace("%object%", o[1].getName())
                if len(msg) > 0:
                    iohandler.setOutput(msg)
                else:
                    iohandler.setOutput(msghandler.getMessage("lookaround-nothing"))

        elif command == "move":
            objects = self.mapmanager.getVisibleObjects()
            obj = None
            msg = ""
            for o in objects:
                direction = o[2]
                objtype = o[0]
                if direction == 1:
                    if objtype == "door":
                        if o[1].getStatus is not "open":
                            msg = msghandler.getMessage("lookaround-nomove") + " "
                            obj = o
                            break
                    else:
                        msg = msghandler.getMessage("lookaround-nomove") + " "
                        obj = o
                        break

            if obj is not None:
                objtype = obj[0]
                if objtype == "wall":
                    msg = msg + msghandler.getMessage("lookaround-front").replace("%object%", msghandler.getMessage("lookaround-wall"))

                elif objtype == "door":
                    if obj[1].getStatus() is not "open":
                        msg = msg + msghandler.getMessage("lookaround-front").replace("%object%", msghandler.getMessage("lookaround-door"))

                elif objtype == "object":
                    msg = msg + msghandler.getMessage("lookaround-front").replace("%object%", obj[1].getName())

            if len(msg) > 0:
                iohandler.setOutput(msg)
            else:
                p = self.mapmanager.getPlayer()
                pos = p.getPosition()
                facing = p.getFacing()

                if facing == "n":
                    pos = [pos[0], pos[1] + 1]
                elif facing == "e":
                    pos = [pos[0] + 1, pos[1]]
                elif facing == "s":
                    pos = [pos[0], pos[1] - 1]
                elif facing == "w":
                    pos = [pos[0] - 1, pos[1]]

                p.setPosition(pos)
                iohandler.setOutput(msghandler.getMessage("lookaround-move"))

        elif command == "goto" and len(args) >= 2:
            pos = [int(args[0]), int(args[1])]

            objatpos = self.mapmanager.objectAtPosition(pos)
            if objatpos is not None:
                iohandler.setOutput(msghandler.getMessage("goto-nomove"))
            else:
                p = self.mapmanager.getPlayer()
                p.setPosition(pos)
                iohandler.setOutput(msghandler.getMessage("goto-move").replace("%x%", args[0]).replace("%y%", args[1]))
            pass

        elif command == "showinventory":
            p = self.mapmanager.getPlayer()
            inv = p.getInventory()
            if len(inv) == 0:
                iohandler.setOutput(msghandler.getMessage("inventory-noitems"))
            else:
                msg = msghandler.getMessage("inventory-show")
                for o in inv:
                    msg = msg + "\n" + o.getName()
                iohandler.setOutput(msg)

        elif command == "door" and len(args) >= 1:
            if not (args[0] == "open" or args[0] == "close"):
                iohandler.setOutput(msghandler.getMessage("general-invalidcommand"))
                return

            objects = self.mapmanager.getVisibleObjects()
            obj = None
            for o in objects:
                direction = o[2]
                objtype = o[0]
                if direction == 1 and objtype == "door":
                    obj = o[1]
                    break

            if obj is None:
                iohandler.setOutput(msghandler.getMessage("door-nodoor"))
                return

            status = obj.getStatus()
            if status == "broken":
                iohandler.setOutput(msghandler.getMessage("door-broken"))
                return

            if args[0] == "open":
                if status == "open":
                    iohandler.setOutput(msghandler.getMessage("door-alreadystatus").replace("%status%", msghandler.getMessage("lookaround-open")))
                    return
                elif type(obj) == CardDoor:
                    p = self.mapmanager.getPlayer()
                    inv = p.getInventory()

                    # Find the highest keycard in inventory
                    keylevel = ""
                    for o in inv:
                        if "-Karte" in o.getName():
                            kl = o.getName().replace("-Karte", "")
                            if len(kl) == 2:
                                if len(keylevel) > 0:
                                    kllist = kl.split('')
                                    keylevellist = keylevel.split('')

                                    if kllist[1] > keylevellist[1]:
                                        keylevel = kl
                                else:
                                    keylevel = kl
                    res = obj.open(keylevel)
                    if not res:
                        iohandler.setOutput(msghandler.getMessage("door-noperm"))
                    else:
                        iohandler.setOutput(msghandler.getMessage("door-action").replace("%action%", msghandler.getMessage("door-opened")))

                # Find a matching door code in the inventory
                elif type(obj) == CodeDoor:
                    p = self.mapmanager.getPlayer()
                    inv = p.getInventory()

                    res = False
                    for o in inv:
                        if "Pincodezettel-" in o.getName():
                            code = o.getName().replace("Pincodezettel-", "")
                            res = obj.open(code)
                            if res:
                                iohandler.setOutput(msghandler.getMessage("door-action").replace("%action%", msghandler.getMessage("door-opened")))
                                return
                    if not res:
                        iohandler.setOutput(msghandler.getMessage("door-noperm"))
                else:
                    obj.open()

            elif args[0] == "close":
                if status == "close":
                    iohandler.setOutput(msghandler.getMessage("door-alreadystatus").replace("%status%", msghandler.getMessage("lookaround-close")))
                    return
                else:
                    obj.close()
                    iohandler.setOutput(
                        msghandler.getMessage("door-action").replace("%action%", msghandler.getMessage("door-closed")))

        elif command == "getposition":
            p = self.mapmanager.getPlayer()
            pos = p.getPosition()

            iohandler.setOutput(msghandler.getMessage("goto-position").replace("%x%", str(pos[0])).replace("%y%", str(pos[1])))

        elif command == "facing":
            p = self.mapmanager.getPlayer()
            facing = p.getFacing()
            facingmsg = msghandler.getMessage("turn-" + facing)
            iohandler.setOutput(msghandler.getMessage("turn-facing").replace("%facing%", facingmsg))

        elif command == "object" and len(args) >= 1:
            if not (args[0] == "showinventory" or args[0] == "getitem" or args[0] == "putitem" or args[0] == "move"):
                iohandler.setOutput(msghandler.getMessage("general-invalidcommand"))
                return
            objects = self.mapmanager.getVisibleObjects()
            obj = None
            for o in objects:
                direction = o[2]
                objtype = o[0]
                if direction == 1 and objtype == "object":
                    obj = o[1]
                    break

            if obj is None:
                iohandler.setOutput(msghandler.getMessage("object-noobject"))
                return

            if args[0] == "showinventory":
                inv = obj.getInventory()
                if len(inv) == 0:
                    iohandler.setOutput(msghandler.getMessage("object-noitems").replace("%objectname%", obj.getName()))
                    return
                else:
                    msg = msghandler.getMessage("object-show").replace("%objectname%", obj.getName())
                    for o in inv:
                        msg = msg + "\n" + o.getName()
                    iohandler.setOutput(msg)

            elif args[0] == "getitem" and len(args) >= 2:
                inv = obj.getInventory()
                p = self.mapmanager.getPlayer()
                pinv = p.getInventory()

                for o in inv:
                    if o.getName() == args[1]:
                        inv.remove(o)
                        obj.setInventory(inv)

                        pinv.append(o)
                        p.setInventory(pinv)

                        iohandler.setOutput(msghandler.getMessage("object-get").replace("%item%", o.getName()).replace("%objectname%", obj.getName()))
                        return
                iohandler.setOutput(msghandler.getMessage("object-noget").replace("%name%", args[1]).replace("%objectname%", obj.getName()))

            elif args[0] == "putitem" and len(args) >= 2:
                inv = obj.getInventory()
                p = self.mapmanager.getPlayer()
                pinv = p.getInventory()

                for o in pinv:
                    if o.getName() == args[1]:
                        pinv.remove(o)
                        p.setInventory(pinv)

                        inv.append(o)
                        obj.setInventory(inv)
                        iohandler.setOutput(msghandler.getMessage("object-put").replace("%item%", o.getName()).replace("%objectname%", obj.getName()))
                        return

                iohandler.setOutput(msghandler.getMessage("object-noput").replace("%name%", args[1]))

            elif args[0] == "move" and len(args) >= 2:
                if not (args[1] == "left" or args[1] == "right" or args[1] == "forward"):
                    iohandler.setOutput(msghandler.getMessage("general-invalidcommand"))
                    return

                p = self.mapmanager.getPlayer()
                ppos = p.getPosition()
                pfacing = p.getFacing()

                if not obj.isMovable():
                    iohandler.setOutput(msghandler.getMessage("object-nomove").replace("%objectname%", obj.getName()))
                    return
                objpos = obj.getPosition()
                postomove = objpos

                if pfacing == "n":
                    if args[1] == "left":
                        postomove = [objpos[0] - 1, objpos[1]]
                    elif args[1] == "right":
                        postomove = [objpos[0] + 1, objpos[1]]
                    elif args[1] == "forward":
                        postomove = [objpos[0], objpos[1] + 1]

                elif pfacing == "e":
                    if args[1] == "left":
                        postomove = [objpos[0], objpos[1] + 1]
                    elif args[1] == "right":
                        postomove = [objpos[0], objpos[1] - 1]
                    elif args[1] == "forward":
                        postomove = [objpos[0] + 1, objpos[1]]

                elif pfacing == "s":
                    if args[1] == "left":
                        postomove = [objpos[0] + 1, objpos[1]]
                    elif args[1] == "right":
                        postomove = [objpos[0] - 1, objpos[1]]
                    elif args[1] == "forward":
                        postomove = [objpos[0], objpos[1] - 1]

                elif pfacing == "w":
                    if args[1] == "left":
                        postomove = [objpos[0], objpos[1] - 1]
                    elif args[1] == "right":
                        postomove = [objpos[0], objpos[1] + 1]
                    elif args[1] == "forward":
                        postomove = [objpos[0] - 1, objpos[1]]

                objatpos = self.mapmanager.objectAtPosition(postomove)
                if objatpos is not None:
                    objname = ""
                    if type(objatpos) == list:
                        objname = msghandler.getMessage("lookaround-wall")
                    elif type(objatpos) == Object:
                        objname = objatpos.getName()
                    else:
                        objname = msghandler.getMessage("lookaround-door")

                    iohandler.setOutput(msghandler.getMessage("object-nomoveblocked").replace("%objectname%", objname))
                    return

                obj.setPosition(postomove)
                dir = msghandler.getMessage("turn-" + args[1])
                iohandler.setOutput(msghandler.getMessage("object-moved").replace("%direction%", dir))

        else:
            iohandler.setOutput(msghandler.getMessage("general-invalidcommand"))


g = GameManager()
g.start()