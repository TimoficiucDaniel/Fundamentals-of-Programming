class Idk:
    def __init__(self, *parameters):
        self.__elements = list(parameters)

    def __setitem__(self, key, value):
        self.__elements[key] = value

    def __getitem__(self, item):
        return self.__elements[item]

    def __delitem__(self, key):
        self.__elements.remove(key)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__elements) - 1:
            raise StopIteration
        self.__index += 1
        return self.__elements[self.__index]

    def gnomeSort(self, list_to_sort, compare):
        index = len(list_to_sort)
        while index < n:
            if index == 0:
                index = index + 1
            if compare(list_to_sort[index], list_to_sort[index - 1]) is True:
                index = index + 1
            else:
                list_to_sort[index], list_to_sort[index - 1] = list_to_sort[index - 1], list_to_sort[index]
                index = index - 1

        return list_to_sort

    def filter(self,list_to_filter,acceptance_function):
        index = 0
        for elements in list_to_filter:
            if acceptance_function(elements) is False:
                list_to_filter.remove(index)
            index +=1
        return list_to_filter



def compare(x, y):
    if x >= y:
        return True
    return False
