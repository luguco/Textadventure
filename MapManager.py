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

        p = jsonmap['people'][0]
        n = jsonmap['people'][1]
        g = jsonmap['people'][2]

        self.player = Player("", p['facing'], [], [p['xpos'], p['ypos']])
        self.narrator = Person("Erzähler", 'narrator', n['facing'], [n['xpos'], n['ypos']])
        self.guard = Person("Wachmann", 'guard', g['facing'], [g['xpos'], g['ypos']])

        # Initialize all objects and subobjects
        for o in jsonmap['objects']:
            obj = Object(o['name'], o['id'], o['movable'], o['pickable'], [], [o['posx'], o['posy']])

            for subo in o['inventory']:
                subobj = Object(subo['name'], subo['id'], subo['movable'], subo['pickable'], [], [o['posx'], o['posy']])
                inv = obj.getInventory()
                inv.append(subobj)
                obj.setInventory(inv)

            self.objects.append(obj)

        # Initialize all doors
        for d in jsonmap['doors']:
            if d['type'] == "card":
                dobj = CardDoor(d['status'], d['direction'], [d['xpos'], d['ypos']], d['authtype'])
                self.doors.append(dobj)
            elif d['type'] == 'code':
                dobj = CodeDoor(d['status'], d['direction'], [d['xpos'], d['ypos']], d['authtype'])
                self.doors.append(dobj)
            elif d['type'] == 'broken' or d['type'] == 'door':
                dobj = Door(d['status'], d['direction'], [d['xpos'], d['ypos']])
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
                res.append([o, index])

        # Find all matching doors at possible coordinates
        for d in self.doors:
            doorcoord = [-1, -1]
            if d.getDirection() == "ns":
                doorpos = d.getPosition()

                # Door is in font of player
                if facing == 'n':
                    doorcoord = [int(doorpos[0]), int(doorpos[1].split('-')[0])]
                    if doorcoord == pos:
                        res.append([d, 1])

                elif facing == 's':
                    doorcoord = [int(doorpos[0]), int(doorpos[1].split('-')[1])]
                    if doorcoord == pos:
                        res.append([d, 1])

                # Door is left or right from player
                elif facing == 'w':
                    doorcoord = [int(doorpos[0]), int(doorpos[1].split('-')[0])]

                    if doorcoord == pos:
                        res.append([d, 2])
                    else:
                        doorcoord = [int(doorpos[0]), int(doorpos[1].split('-')[1])]
                        if doorcoord == pos:
                            res.append([d, 0])

                elif facing == "e":
                    doorcoord = [int(doorpos[0]), int(doorpos[1].split('-')[0])]

                    if doorcoord == pos:
                        res.append([d, 0])
                    else:
                        doorcoord = [int(doorpos[0]), int(doorpos[1].split('-')[1])]
                        if doorcoord == pos:
                            res.append([d, 2])

            elif d.getDirection() == "we":
                doorpos = d.getPosition()

                # Door is in front of player
                if facing == 'w':
                    doorcoord = [int(doorpos[0].split('-')[1]), int(doorpos[1])]
                    if doorcoord == pos:
                        res.append([d, 1])

                elif facing == 'e':
                    doorcoord = [int(doorpos[0].split('-')[0]), int(doorpos[1])]
                    if doorcoord == pos:
                        res.append([d, 1])

                # Door is left or right from player
                elif facing == 'n':
                    doorcoord = [int(doorpos[0].split('-')[0]), int(doorpos[1])]
                    if doorcoord == pos:
                        res.append([d, 2])
                    else:
                        doorcoord = [int(doorpos[0].split('-')[1]), int(doorpos[1])]
                        if doorcoord == pos:
                            res.append([d, 0])

                elif facing == 's':
                    doorcoord = [int(doorpos[0].split('-')[0]), int(doorpos[1])]
                    if doorcoord == pos:
                        res.append([d, 0])
                    else:
                        doorcoord = [int(doorpos[0].split('-')[1]), int(doorpos[1])]
                        if doorcoord == pos:
                            res.append([d, 2])

        return None

    def getPlayer(self):
        return self.player

    def objectAtPosition(self, pos: list)-> bool:
        for o in self.objects:
            if o.getPosition() == pos:
                return True

        if self.player.getPosition() == pos:
            return True

        if self.guard.getPosition() == pos:
            return True

        if self.narrator.getPosition() == pos:
            return True

        return False

