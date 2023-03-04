from repository.RepoException import RepoError


class Repository:
    """
    Repository template used for all the different classes in domain
    """

    def __init__(self):
        self._object_list = []

    def find(self, object):
        """
        function that searches the object in the object repo by its id and returns it if it is found, otherwise 0
        :param object:
        :return:
        """
        for objects in self._object_list:
            if str(object.id) == str(objects.id):
                return object
        return None

    def delete(self, object):
        """
        function that deletes the object from the object repo, raises error if object does not appear in repo
        :param object:
        :return:
        """
        object_to_delete = self.find(object)
        if object_to_delete is None:
            raise RepoError(">object does not appear in repository")
        self._object_list.remove(object_to_delete)

    def add(self, object):
        """
        function that adds an object to the repo , raises error if object appears already in repo(unique ids)
        :param object:
        :return:
        """
        object_to_add = self.find(object)
        if object_to_add is not None:
            raise RepoError([">object already in repository"])
        self._object_list.append(object)

    def find_index(self, object):
        """
        function that searches and returns the index of an object in the repo
        :param object:
        :return:
        """
        index = 0
        for objects in self._object_list:
            if object.id == objects.id:
                return index
            index += 1

    def update(self, object):
        """
        function that updates an object in the repo with new data
        :param object:
        :return:
        """
        object_to_update = self.find(object)
        if object_to_update is None:
            raise RepoError([">nothing to update"])
        object_to_update_index = self.find_index(object_to_update)
        self._object_list.pop(object_to_update_index)
        self._object_list.insert(object_to_update_index, object)

    @property
    def object_list(self):
        return self._object_list

    def __str__(self):
        r = ""
        for objects in self._object_list:
            r += str(objects)
            r += "\n"
        return r
