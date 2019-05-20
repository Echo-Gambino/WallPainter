
import numpy as np

class Link:

    def __init(self):
        self._InfoNode = [None, None]
        self._Cost = 0

    def getNodes(self):
        return self._InfoNode

    def setNodes(self, infoNode):
        self._InfoNode = infoNode

    def getCost(self):
        return self._Cost

    def setCost(self, cost):
        self._cost = cost



class Node:

    def __int__(self):
        self._value = 0

        self._Coords = (-1, -1)

        self._Link = dict()
        self._Link["Left"] = None
        self._Link["Right"] = None
        self._Link["Up"] = None
        self._Link["Down"] = None

        return

    def getValue():
        return self._value

    def setValue(value):
        self._value = value

    def getCoords(self):
        return self._Coords

    def setCoords(self, coords):
        self._Coords = coords

    def getLink(self, direction):
        return self._Link[direction]

    def setLink(self, direction, link):
        self._Link[direction] = link


class graphMaker:

    def __init__(self):
        self.linkList = dict()
        self.nodeList = dict()
        self.height = 0
        self.width = 0

        return
"""
    def constructGraph(self, array):

        if (len(array) <= 0):
            print("ERROR: The length of array is 0, aborting task")
            return
        
        height = len(array)
        width = len(array[0])

        last_coords = (-1, -1)
        node = None

        for y in range(height):
            for x in range(width):
                currNode = None
                leftNode = Non
                
                node.setCoords((x, y))

        print(len(array))
        print(len(array[0]))

        return
"""

    def constructGraph(self, array):

        if len(array) <= 0:
            return False

        self.height = len(array)
        self.width = len(array[0])

        self._makeNode((0, 0), array)

        return True

    def _makeNode(self, (x, y), array):
        # Make the node
        node = Node()
        node.setValue(array[x][y])
        node.setCoords((x, y))

        # Place it into the dictionary
        self.nodeList[(x, y)] = node

        directions = 
        [
                ("Up", (x, y + 1)),
                ("Down", (x, y - 1)),
                ("Right", (x + 1, y)),
                ("Left", (x - 1, y))
        ]

        for (d, (x0, y0)) in directions:
            if self.nodeList[(x0, y0)] is not None:
                continue

            value = -1
            try:
                value = array[x0][y0]
            except:
                continue
            
            new_node = self._makeNode((x0, y0), array)

            if new_node is None:
                continue

            # Link the two nodes together
            cost = []
            if (d == "Up"):
                cost = [1+2, 1+0]
            elif (d == "Down"):
                cost = [1+0, 1+2]
            elif (d == "Right"):
                cost = [1+1, 1+1]
            elif (d == "Left"):
                cost = [1+1, 1+1]

            # Make the links (forward and backward)
            link0 = Link()
            link0.setNodes([node, new_node])
            link0.setCost(cost[0])
            link1 = Link()
            link1.setNodes([node, new_node])
            link1.setCost(cost[1])

            # Place in link list
            self.linkList[(x, y), (x0, y0)] = link0
            self.linkList[(x0, y0), (x, y)] = link1

        return node

    def test(self):
        return

    def makeNodeStrip(self):
        return

    def makeLinkStrip(self):
        return



if (__name__ == "__main__"):

    arrayR = np.array(
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 1]
            ]
            )

    print(arrayR)

    print()

    print(arrayR[0][0])


    g = graphMaker()

    g.constructGraph(arrayR)
