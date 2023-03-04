from services.ClientService import ClientService
from services.MovieService import MovieService
from services.RentalService import RentalService


class UndoRedo:

    def __init__(self, undo_history_list, redo_history_list, client_service, movie_service, rental_service):
        self.__client_service = client_service
        self.__movie_service = movie_service
        self.__rental_service = rental_service
        self.__undo_history_list = undo_history_list
        self.__redo_history_list = redo_history_list
        self.__index = -1

    def add_to_undo_history(self, object):
        self.__undo_history_list.append(object)
        self.__index += 1
        self.__redo_history_list.clear()

    def undo(self):
        if self.__index < 0:
            raise ValueError(">no undo")
        for actions in self.__undo_history_list[self.__index].command_block:
            if actions.command_name == 'create_client':
                self.__client_service.create(actions.parameters.parameter1
                                             , actions.parameters.parameter2)
            elif actions.command_name == 'create_rental':
                self.__rental_service.create_rental(actions.parameters.parameter1
                                                    , actions.parameters.parameter2
                                                    , actions.parameters.parameter3
                                                    , actions.parameters.parameter4
                                                    , actions.parameters.parameter5
                                                    , actions.parameters.parameter6)
            elif actions.command_name == 'delete_client':
                self.__client_service.delete(actions.parameters.parameter1)
            elif actions.command_name == 'delete_movie':
                self.__movie_service.delete(actions.parameters.parameter1)
            elif actions.command_name == 'create_movie':
                self.__movie_service.add(actions.parameters.parameter1
                                         , actions.parameters.parameter2
                                         , actions.parameters.parameter3
                                         , actions.parameters.parameter4)
            elif actions.command_name == 'delete_rental':
                self.__rental_service.delete(actions.parameters.parameter1)
            elif actions.command_name == 'update_client':
                self.__client_service.update(actions.parameters.parameter1,
                                             actions.parameters.parameter2)
            elif actions.command_name == 'update_movie':
                self.__movie_service.update(actions.parameters.parameter1
                                            , actions.parameters.parameter2
                                            , actions.parameters.parameter3
                                            , actions.parameters.parameter4)
        self.__index += -1
        self.__undo_history_list.pop(-1)
