#modula for python abstract class
from _py_abc import ABCMeta


class PlayerClass(object):

    totalPlayer = 0

    def __init__(self):
        PlayerClass.totalPlayer += 1
        self.name = "player"+ str(PlayerClass.totalPlayer)

    def talk(self):
        print("talk")


class Player(object):

    totalPlayer = 0

    def __init__(self):
        PlayerClass.totalPlayer += 1
        self.name = "player" + str(PlayerClass.totalPlayer)

    def talk(self):
        print("Hello")

#python abstract class
class Shape(object):
    __metaclass__=ABCMeta

    def __init__(self):
        self.color="blue"

    def draw(self):
        pass

