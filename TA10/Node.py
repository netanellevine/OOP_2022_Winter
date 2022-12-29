import json
import random
from concurrent.futures import ThreadPoolExecutor


class Node:

    def __init__(self, index, weight, color, x, y):
        self.__index = index
        self.__x = x
        self.__y = y
        self.in_deg = 0
        self.out_deg = 0
        self.weight = weight
        self.color = color

    def getIndex(self):
        return self.__index

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getInDegree(self):
        return self.in_deg

    def getOutDegree(self):
        return self.out_deg

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getWeight(self):
        return self.weight

    def setWeight(self, w):
        self.weight = w

    def __repr__(self) -> str:
        return f'Node: id: {self.__index}, (x,y): ({self.__x},{self.__y}), in_deg: {self.in_deg}, out_deg: ' \
               f'{self.out_deg}, weight: {self.weight}, color: {self.color}'


counter = 0


def getRandomNode():
    global counter
    color = random.randint(-1, 1)
    weight = random.random()
    weight = abs(weight)
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    n = Node(counter, weight, color, x, y)
    counter += 1
    return n


def getRandomNodeList(n):
    # output = []
    # for i in range(n):
    #     output.append(getRandomNode())
    # return output
    return [getRandomNode() for _ in range(n)]


def toJson(n: Node):
    data = {
        "index": n.getIndex(),
        "x": n.getX(),
        "y": n.getY(),
        "weight": n.getWeight(),
        "color": n.getColor(),
        "in_deg": n.getInDegree(),
        "out_deg": n.getOutDegree()
    }

    filename = str(n.getIndex()) + ".json"
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4)


if __name__ == '__main__':
    lst = getRandomNodeList(20)
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread1 = executor.map(toJson, lst)
