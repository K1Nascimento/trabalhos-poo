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
        class Quadrilatero:
    def __init__(self, p1,p2): 
        self.p1 = p1
        self.p2 = p2

    def verificaQuadrilatero(self): 
        if self.p1.getX() < self.p2.getX() and self.p1.getY() > self.p2.getY():
         return True
        return False
    def contidoEmQ(self, p3): 
        if p3.getX() > self.p1.getX() and p3.getX() < self.p2.getX() and p3.getY() < self.p1.getY() and p3.getY() > self.p2.getY():
         return True
        return False    
