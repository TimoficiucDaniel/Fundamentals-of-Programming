from domain import ValidatorException


class Client:
    """
    Class client which holds the client id and his name
    """

    def __init__(self, client_id, name):
        self._client_id = client_id
        self._name = name

    def __str__(self):
        return "Client id is : " + str(self._client_id) + " and his name is : " + str(self._name)

    def __repr__(self):
        return "Client id is : " + str(self._client_id) + " and his name is : " + str(self._name)

    @property
    def id(self):
        return str(self._client_id)

    @property
    def name(self):
        return self._name


class ClientValidator:
    @staticmethod
    def validate(client):
        if isinstance(client, Client) == False:
            raise TypeError(">can only validate client objects")
        _errors = []
        if client.id.isnumeric() is False:
            _errors.append(">client id must be an integer number")
        if len(client.id) != 5:
            _errors.append(">incorrect id format")
        if len(_errors) > 0:
            raise ValidatorException.ValidatorError(_errors)
