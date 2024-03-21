class P:

    def __init__(self,x):
        self.__setX(x)

    def __getX(self):
        return self.__x

    def __setX(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__getX, __setX)


class P2:

    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


# pruebas con la clase P
print ("Con la clase P: ")
p = P(300)
print (p.x)
p.x = 400
print (p.x)

# Pruebas con la clase P2
print ("Con la clase P2: ")
p2 = P2(300)
print (p2.x)
p2.x = 400
print (p2.x)

