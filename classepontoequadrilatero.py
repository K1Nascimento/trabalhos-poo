class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def qualQuadrante(self, x, y):
        if (x > 0 and y > 0):
            return 1
        if (x < 0 and y > 0):
            return 2
        if (y < 0 and x < 0):
            return 3
        if (y < 0 and x > 0):
            return 4
        if (y == 0 and x == 0):
            return