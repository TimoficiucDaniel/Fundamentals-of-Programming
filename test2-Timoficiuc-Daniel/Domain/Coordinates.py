class Coordinate:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return int(self.__x)

    @property
    def y(self):
        return int(self.__y)

    def __str__(self):
        return "Coordinates are x = " + str(self.__x) + " and y = " + str(self.__y)

    def __repr__(self):
        return "Coordinates are x = " + str(self.__x) + " and y = " + str(self.__y)