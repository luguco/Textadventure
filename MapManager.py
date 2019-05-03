from Player import *
from Person import *
from Object import *
from CardDoor import *
from CodeDoor import *


class MapManager(object):

    def __init__(self, jsonmap):
        # Initialize all variables
        self.objects = []
        self.doors = []
        self.walls = jsonmap['walls']

        p = jsonmap['people'][0]
        n = jsonmap['people'][1]
        g = jsonmap['people'][2]
        # TODO: ADD INVENTORY ITEMS TO PLAYER

        self.player = Player("", p['facing'], [], [p['xpos'], p['ypos']])
        self.narrator = Person("Erzähler", 'narrator', n['facing'], [n['xpos'], n['ypos']])
        self.guard = Person("Wachmann", 'guard', g['facing'], [g['xpos'], g['ypos']])

        # Initialize default inventory items:
        inv = []
        for o in p['inventory']:
            obj = Object(o['name'], o['id'], False, True, [], None)
            inv.append(obj)
        self.player.setInventory(inv)

        # Initialize all objects and subobjects
        for o in jsonmap['objects']:
            obj = Object(o['name'], o['id'], o['movable'], o['pickable'], [], [o['posx'], o['posy']])

            for subo in o['inventory']:
                subobj = Object(subo['name'], subo['id'], False, True, [], None)
                inv = obj.getInventory()
                inv.append(subobj)
                obj.setInventory(inv)

            self.objects.append(obj)

        # Initialize all doors
        for d in jsonmap['doors']:
            if d['type'] == "card":
                dobj = CardDoor(d['status'], [d['xpos'], d['ypos']], d['authtype'], d['name'])
                self.doors.append(dobj)

            elif d['type'] == 'code':
                dobj = CodeDoor(d['status'], [d['xpos'], d['ypos']], d['authtype'], d['name'])
                self.doors.append(dobj)

            elif d['type'] == 'broken' or d['type'] == 'door':
                dobj = Door(d['status'], [d['xpos'], d['ypos']], d['name'])
                self.doors.append(dobj)

    def getVisibleObjects(self):
        facing = self.player.getFacing()
        pos = self.player.getPosition()

        res = []
        # Possible coordinates for objects around the player with a distance of 1
        # and relative to the player on the left, front and right
        # [left, front, right]
        coordpos = [[-1, -1]]
        if facing == 'n':
            coordpos = [[pos[0] - 1, pos[1]],
                        [pos[0], pos[1] + 1],
                        [pos[0] + 1, pos[1]]
                        ]

        elif facing == 's':
            coordpos = [[pos[0] + 1, pos[1]],
                        [pos[0], pos[1] - 1],
                        [pos[0] - 1, pos[1]]
                        ]

        elif facing == 'w':
            coordpos = [[pos[0], pos[1] - 1],
                        [pos[0] - 1, pos[1]],
                        [pos[0], pos[1] + 1]
                        ]

        elif facing == 'e':
            coordpos = [[pos[0], pos[1] + 1],
                        [pos[0] + 1, pos[1]],
                        [pos[0], pos[1] - 1]
                        ]

        # Find all matching objects at possible coordinates
        for o in self.objects:
            if o.getPosition() in coordpos:
                index = coordpos.index(o.getPosition())
                res.append(['object', o, index])

        # Find all matching doors at possible coordinates
        for d in self.doors:
            if d.getPosition() in coordpos:
                index = coordpos.index(d.getPosition())
                res.append(['door', d, index])

        # Find all matching walls at possible coordinates
        for w in self.walls:
            if w in coordpos:
                index = coordpos.index(w)
                res.append(['wall', w, index])

        return res

    def getPlayer(self):
        return self.player

    def rotatePlayer(self, direction):
        facing = self.player.getFacing()

        if direction == "right":
            if facing == "n":
                facing = "e"
            elif facing == "e":
                facing = "s"
            elif facing == "s":
                facing = "w"
            elif facing == "w":
                facing = "n"

        elif direction == "left":
            if facing == "n":
                facing = "w"
            elif facing == "w":
                facing = "s"
            elif facing == "s":
                facing = "e"
            elif facing == "e":
                facing = "n"
        self.player.setFacing(facing)

    def objectAtPosition(self, pos: list)-> object:
        for o in self.objects:
            if o.getPosition() == pos:
                return o

        for d in self.doors:
            if d.getPosition() == pos and d.getStatus() is not "open":
                return d

        for w in self.walls:
            if w == pos:
                return w

        if self.guard.getPosition() == pos:
            return self.guard

        if self.narrator.getPosition() == pos:
            return self.narrator

        return None

