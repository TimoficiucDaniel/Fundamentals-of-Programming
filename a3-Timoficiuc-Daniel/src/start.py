import functions
import copy


def init_list():
    """
    -initializes the main list which is composed of lists , each beginning with one of the specified categories
    -each category list then contains lists of the form [day,sum]
    """
    return [["housekeeping", [20, 25], [16, 29]], ["food", [20, 250], [1, 300]], ["transport", [12, 34], [4, 2]],
            ["clothing", [4, 30], [16, 500],[5,25]], ["internet", [18, 90]], ["others", [18, 200]]]


def command_split(command):
    """
    -function called after input
    -removes whitespaces before and after input
    -splits the input into command_word used to call different functions and command_parameters which are the parameters
    """
    command = command.strip()
    # strips whitespaces
    aux = command.split(sep=' ', maxsplit=1)
    # splits the input
    return [aux[0].strip().lower(), aux[1].strip().lower()] if len(aux) == 2 else [aux[0].strip().lower(), None]
    # returns command_word ,command_param if command param is not empty

def update_undo(content_list,undo_list):
    new_list=copy.deepcopy(content_list)
    undo_list.append(new_list)

def start():
    """
    -main function
    -called at the start of the program
    -calls different functions based on input
    -prints errors which have been raised
    """
    undo_list=[]
    content_list = init_list()
    undo_list.append(init_list())
    while True:
        command = input("prompt>")
        command_word, command_params = command_split(command)
        try:
            if command_word == 'add':
                functions.add_to_list(command_params, content_list)
                update_undo(content_list,undo_list)
            elif command_word == 'insert':
                functions.insert_to_list(command_params, content_list)
                update_undo(content_list,undo_list)
            elif command_word == 'remove':
                functions.remove_list(command_params, content_list)
                update_undo(content_list,undo_list)
            elif command_word == 'list':
                functions.show_list(command_params, content_list)
            elif command_word == 'sum' :
                functions.show_sum_category(command_params,content_list)
            elif command_word == 'max':
                functions.find_max(command_params,content_list)
            elif command_word == 'sort':
                functions.sort_day(command_params,content_list)
            elif command_word == 'filter':
                functions.filter(command_params,content_list)
                update_undo(content_list, undo_list)
                elif command_word == 'undo':
                content_list=functions.undo_list(command_params,content_list,undo_list)
            elif command_word == 'exit':
                return
            else:
                print(">command does not exist")
        except ValueError as ve:
            print(str(ve))


start()
