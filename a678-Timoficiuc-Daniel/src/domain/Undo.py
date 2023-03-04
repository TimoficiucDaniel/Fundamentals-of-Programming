class UndoRedoCommandBlock:
    def __init__(self):
        self._command_block = []

    def add_to_block(self,object):
        self._command_block.append(object)

    @property
    def command_block(self):
        return self._command_block

class UndoRedoActions:
    def __init__(self,command_name,parameters):
        self.__command_name = command_name
        self.__parameters = parameters

    @property
    def command_name(self):
        return self.__command_name

    @property
    def parameters(self):
        return self.__parameters

class Parameter:
    def __init__(self,parameter1,parameter2,parameter3,parameter4,parameter5,parameter6):
        self.__parameter1 = parameter1
        self.__parameter2 = parameter2
        self.__parameter3 = parameter3
        self.__parameter4 = parameter4
        self.__parameter5 = parameter5
        self.__parameter6 = parameter6

    @property
    def parameter1(self):
        return self.__parameter1

    @property
    def parameter2(self):
        return self.__parameter2

    @property
    def parameter3(self):
        return self.__parameter3

    @property
    def parameter4(self):
        return self.__parameter4

    @property
    def parameter5(self):
        return self.__parameter5

    @property
    def parameter6(self):
        return self.__parameter6