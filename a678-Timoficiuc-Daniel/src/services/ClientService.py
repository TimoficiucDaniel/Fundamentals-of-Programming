from domain.Client import Client
from domain.Undo import UndoRedoActions
from domain.Undo import Parameter
from domain.Undo import UndoRedoCommandBlock


class ClientService:
    """
    client service class used to call functions that create,delete,read,update in the client repo
    """

    def __init__(self, client_repo, rental_repo, validator):
        self._client_repo = client_repo
        self._rental_repo = rental_repo
        self._validator = validator

    def create(self, client_id, name):
        """
        function that creates a new object based on the parameters,validates it
         and calls the add function from the repo with this new object
        :param client_id:
        :param name:
        :return:
        """
        block = UndoRedoCommandBlock()
        client = Client(client_id, name)
        self._validator.validate(client)
        param = Parameter(str(client_id), name, None, None, None, None)
        actions = UndoRedoActions('delete_client', param)
        block.add_to_block(actions)
        self._client_repo.add(client)
        return block

    def delete(self, client_id):
        """
        function that deletes a client from the client repo and then deletes all rentals related to that client
        :param client_id:
        :return:
        """
        block = UndoRedoCommandBlock()
        aux = False
        for clients in self._client_repo.object_list:
            if client_id == clients.id:
                id = clients.id
                name = clients.name
                self._client_repo.delete(clients)
                aux = True
                param = Parameter(id, name, None, None, None, None)
                action = UndoRedoActions('create_client', param)
                block.add_to_block(action)
        for rentals in self._rental_repo.object_list:
            if client_id == rentals.client_id:
                self._rental_repo.delete(rentals)
                id1 = rentals.id
                id2 = rentals.movie_id
                id3 = rentals.client_id
                rented_date = rentals.rented_date
                due_date = rentals.due_date
                returned_date = rentals.returned_date
                param = Parameter(str(id1), str(id2), str(id3), rented_date, due_date, returned_date)
                action = UndoRedoActions('create_rental', param)
                block.add_to_block(action)
        if aux is False:
            raise ValueError("No client to delete")
        return block

    def update(self, client_id, name):
        """
        function that creates a new object with the same id as the one to be updated and then calls the
         update function from repo with this new object with updated data
        :param client_id:
        :param name:
        :return:
        """
        block = UndoRedoCommandBlock()
        client = Client(client_id, name)
        self._validator.validate(client)
        for clients in self._client_repo.object_list:
            if clients.id == client_id:
                id = clients.id
                name = clients.name
                param = Parameter(str(id), name, None, None, None, None)
                action = UndoRedoActions('update_client', param)
                block.add_to_block(action)
        self._client_repo.update(client)
        return block

    def list(self):
        return str(self._client_repo)

    def search_by_name(self, input_to_search_by):
        input_to_search_by = input_to_search_by.strip()
        new_list = []
        for clients in self._client_repo.object_list:
            if input_to_search_by.lower() in clients.name.lower():
                new_list.append(clients)
        return new_list

    def search_by_id(self, input_to_search_by):
        input_to_search_by = input_to_search_by.strip()
        new_list = []
        for clients in self._client_repo.object_list:
            if input_to_search_by == clients.id:
                new_list.append(clients)
        return new_list
