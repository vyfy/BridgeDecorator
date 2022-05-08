#!/usr/bin/python
# Authoer: Spencer.Luo
# Date: 7/8/2018

# Version 1.0
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Введение ABCMeta и abstractmethod для определения абстрактных классов и абстрактных методов.

class Shape(metaclass=ABCMeta):
    """форма"""

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        return self._color.getColor() + self.getShapeType()


class Rectange(Shape):
    """прямоугольник"""

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return " прямоугольник "

class Ellipse(Shape):
    """овал"""

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return " овал "

class Color(metaclass=ABCMeta):
    """цвет"""

    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    """красный"""

    def getColor(self):
        return " красный "


class Green(Color):
    """зеленый"""

    def getColor(self):
        return " зеленый "

def testShap():
    redRect = Ellipse(Red())
    strs = redRect.getShapeInfo()

    return strs


testShap()
