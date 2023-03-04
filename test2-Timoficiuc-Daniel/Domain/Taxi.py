class Taxi:
    def __init__(self, id, fare, coordinates):
        self.__id = id
        self.__fare = fare
        self.__coordinates = coordinates

    @property
    def id(self):
        return self.__id

    @property
    def fare(self):
        return self.__fare

    @property
    def coordinates(self):
        return self.__coordinates

    @fare.setter
    def fare(self, value):
        self.__fare = value

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    def __str__(self):
        return "Taxi id is : " + str(self.__id) + " and its fare is : " + str(self.__fare) + ",coordinates are " \
               + str(self.__coordinates)

    def __repr__(self):
        return "Taxi id is : " + str(self.__id) + " and its fare is : " + str(self.__fare) + ",coordinates are " \
               + str(self.__coordinates)
