class Repository:
    def __init__(self):
        self._object_list = []

    def add(self, object):
        self._object_list.append(object)

    @property
    def object_list(self):
        return self._object_list

    def __str__(self):
        r = ""
        for objects in self._object_list:
            r += str(objects)
            r += "\n"
        return r
