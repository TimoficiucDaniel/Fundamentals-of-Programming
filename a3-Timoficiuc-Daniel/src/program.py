from datetime import date

"""
  Write non-UI functions below
"""


def test_create_add():
    assert create_list_add([10, 'food']) == [22, 10]
    assert create_list_add([20, 'clothing']) == [22, 20]
    assert create_list_add([30, 'others']) == [22, 30]
    assert create_list_add([40, 'housekeeping']) == [22, 40]
    assert create_list_add([50, 'transport']) == [22, 50]


def test_create_insert():
    assert create_list_insert(([10, 25])) == [10, 25]
    assert create_list_insert(([12, 30])) == [12, 30]
    assert create_list_insert(([15, 2])) == [15, 2]
    assert create_list_insert(([30, 25])) == [30, 25]
    assert create_list_insert(([20, 16])) == [20, 16]
    assert create_list_insert(([8, 14])) == [8, 14]


def remove_list(command_params, content_list):
    """
    -this function is called by the command menu function
    -checks if the parameters received are empty, raises error if so
    -calls 3 different functions based on the parameters received
    -each function called checks a functionality listed in the problem
    remove <day>
    remove <start day> to <end day>
    remove <category>

    """
    check_if_empty(command_params)
    param = command_params.split(' ')
    # splits command_params into a list of words
    params = []
    for word in param:
        if word != "":
            params.append(word)
            # removes the whitespaces which happen to be interpreted as a word in the list
    if len(params) > 1:
        # if the function has multiple parameters it calls the remove_days function
        remove_days(params, content_list)
    elif param[0].isnumeric() is True:
        # if the function parameter is numeric it calls the remove_day function
        remove_day(params, content_list)
    else:
        remove_category(params, content_list)
        # if none of the other are true it calls the remove category function


def check_error_remove_days(params):
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
        # checks for appropriate number of parameters,raises error if not
        # enough or too many parameters
    if params[1] != "to":
        raise ValueError(">invalid operation")
        # checks if the second parameter is the word "to", raises error if not"to"
    if int(get_day_list(params)) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
        # checks if the day1 parameter is from [1,30],raises
        # error otherwise
    if int(get_day2(params)) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
        # checks if the day2 parameter is from [1,30],raises
        # error otherwise
    if int(get_day_list(params)) == int(get_day2(params)) or abs(
            int(get_day2(params)) - int(get_day_list(params))) == 1:
        # checks if the days are equal ore are consecutive,
        # raises error if so since we remove the days fromm the interval (day1,day2)
        raise ValueError(">days cannot be the same or consecutive")


def swap_days(day1, day2):
    return params[2], params[0]
    # swaps day1 day2 parameters around if day2 < day1


def remove_days(params, content_list):
    """
    -this function is called by the main remove_list function
    -checks for input errors such as number of param, type etc
    -removes items from the main list whose day param is between day1,day2 parameters of this function
    remove <start day> to <end day> -parameters
    """
    check_error_remove_days(params)
    if int(get_day2(params)) < int(get_day_list(params)):
        params[0], params[2] = swap_days(params[0], params[2])
        # swaps day1 day2 parameters around if day2 < day1
    ok = False
    # aux to check if day appears in the list
    for lists in content_list:
        counter = 0
        # counter used to pop elements from the list
        for nested_list in list(lists):
            # list(lists) creates a copy of lists which we iterate so that when we pop items
            # we do not have problems with iteration
            if str(get_day_list(nested_list)).isnumeric() is True:
                if int(get_day_list(params)) < get_day_list(nested_list) and int(get_day2(params)) > get_day_list(
                        nested_list):
                    ok = True
                    lists.pop(counter)
                    counter -= 1
                    # if the day is in the interval we pop the list [day,sum] from the main list and decrement
                    # counter by 1 to match the shift of indexes
            counter += 1
    if ok is False:
        raise ValueError(">day does not appear anywhere")
        # raise error if no days were removed


def get_day2(params):
    # getter
    return params[2]


def check_error_remove_day(params):
    x = get_day_list(params)
    if int(x) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
        # checks if day param is in the correct interval
        # raises error if not


def remove_day(params, content_list):
    """
    -function called by the remove_list function
    -removes all items from the main list whose day param is equal to a certain day from input
    -checks for errors
    remove <day> -parameters
    """
    check_error_remove_day(params)
    ok = False
    # aux to check if the certain day appears anywhere in the list
    for lists in content_list:
        counter1 = 0
        counter2 = 0
        for nested_list in list(lists):
            # list(lists) creates a copy of lists which we iterate so that when we pop items
            # we do not have problems with iteration
            if str(get_day_list(params)) == str(get_day_list(nested_list)):
                ok = True
                lists.pop(counter1)
                counter1 -= 1
                # pops the certain item [day,sum] from the list whose day param is equal to the specified one
            counter1 += 1
            counter2 += 1
    if ok is False:
        raise ValueError(">day does not appear anywhere")
        # raises error if no days were removed


def remove_category(params, content_list):
    """
    -function called by the remove_list function
    -removes all elements from a list corresponding to the specified category
    remove <category> -parameters
    """
    counter = False
    # aux used to check if category exists
    for lists in content_list:
        if get_category(lists) == get_category(params):
            counter = True
            x = get_category(params)
            lists.clear()
            lists.append(x)
            # function remembers the first element of the list which is always the category then
            # clears the list and inserts the category back into the first spot in the list
    if counter is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist


def check_if_empty(command_params):
    if command_params is None:
        raise ValueError(">parameters not specified")
    # raises error if parameters are empty


def check_error_insert_to_list(params):
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
    # raises error if there are too many or too few parameters
    x = get_sum_insert(params)
    if x.isnumeric() is False:
        raise ValueError(">sum has to be an integer")
    # raises error if sum parameter is not an integer
    y = get_day_insert(params)
    if y.isnumeric() is False:
        raise ValueError(">day has to be an integer")
    # raises error if day parameter is not an integer
    if int(y) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
    # raises error if day parameter is not in the correct interval


def insert_to_list(command_params, content_list):
    """
    -function that inserts a sum at a certain day into a certain category in the main list
    -checks for input errors
    -insert <day> <sum> <category> -parameters
    """
    check_if_empty(command_params)
    param = command_params.split(' ')
    # splits the command parameters into a list of words
    params = []
    for word in param:
        if word != "":
            params.append(word)
            # function that removes the whitespaces that happen to be interpreted as words
    check_error_insert_to_list(params)
    ok = False
    # aux used to check if category appears in the list
    for lists in content_list:
        if get_category_insert(params) == get_category(lists):
            ok = True
            aux = create_list_insert(params)
            # calls a function that creates the specified [day,sum] list
            lists.append(aux)
            # appends list to the specified category in the main list
    if ok is False:
        raise ValueError(">category does not exist")
    # raises error if the category does not exist


def create_list_insert(params):
    """
    -called by the insert_to_list function
    -returns a list composed of day and sum parameters
    """
    aux = []
    aux.append(get_day_insert(params))
    aux.append(get_sum_insert(params))
    return aux


def get_day_list(lists):
    # getter
    return lists[0]


def get_category_insert(params):
    # getter
    return params[2]


def get_sum_insert(params):
    # getter
    return params[1]


def get_day_insert(params):
    # getter
    return params[0]


def get_category(lists):
    # getter
    return lists[0]


def get_category_add(params):
    # getter
    return params[1]


def get_sum_add(params):
    # getter
    return params[0]


def create_list_add(params):
    """
    -function called by the add_to_list function
    -returns a list composed of the current date day and the sum
    -current date day is obtained using .today() function from the datetime module
    """
    aux = []
    today = date.today()
    aux.append(today.day)
    aux.append(get_sum_add(params))
    return aux


def init_list():
    """
    -initializes the main list which is composed of lists , each beginning with one of the specified categories
    -each category list then contains lists of the form [day,sum]
    """
    return [["housekeeping", [20, 25], [16, 29]], ["food", [20, 250], [1, 300]], ["transport", [12, 34], [4, 2]],
            ["clothing", [4, 30], [16, 500]], ["internet", [18, 90]], ["others", [18, 200]]]


def check_error_add_to_list(params):
    if len(params) != 2:
        raise ValueError(">incorrect parameters")
    # raises error if there are too many or too few parameters
    x = get_sum_add(params)
    if x.isnumeric() is False:
        raise ValueError(">sum has to be an integer")
    # raises error if sum parameter is not an integer


def add_to_list(command_params, content_list):
    """
    -function which adds a sum to a category using the current date from the calendar
    -checks for input errors
    add <sum> <category> -parameters
    """
    check_if_empty(command_params)
    param = command_params.split(' ')
    # splits the command parameters into a list of words
    params = []
    for word in param:
        if word != "":
            params.append(word)
            # function that removes the whitespaces that happen to be interpreted as words
    check_error_add_to_list(params)
    aux = create_list_add(params)
    # calls a function which creates the desired list of the form [current_date.day,sum]
    counter = False
    # aux used to check if category appears in the main list
    for lists in content_list:
        if get_category_add(params) == get_category(lists):
            counter = True
            lists.append(aux)
            # appends the [day,sum] list to the category list
    if counter is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist


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


def get_operation(params):
    # getter
    return params[1]


def check_error_show_category_relations(params):
    aux = ["=", "<", ">"]
    # list containing the three possible relations
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
    # raises error if too many or too few parameters
    if get_operation(params) not in aux:
        raise ValueError(">incorrect operation")
    # raises error if the relation parameter is not in the relation list
    if params[2].isnumeric() is False:
        raise ValueError(">sum has to be an integer")
    # raises error if the sum parameter is not an integer


"""
  Write the command-driven UI below
"""


def show_category_relations(params, content_list):
    """
    -function called by the show_list function
    -prints all items from a category list with a certain relation to the input
    list <category> [ < | = | > ] <value> - parameters
    -relations can be =,<,>
    """
    aux = ["=", "<", ">"]
    check_error_show_category_relations(params)
    # list containing the three possible relations
    ok = False
    # aux used to check if category exists
    counter = False
    # aux used to check if there are any lists that could be printed
    for lists in content_list:
        if get_category(lists) == get_category(params):
            ok = True
            print("Category: " + str(get_category(lists)))
            print("==========================")
            print("")
            for nested_list in lists:
                if nested_list != lists[0]:
                    if get_operation(params) == aux[0]:
                        # checks if relation is '='
                        if int(params[2]) == get_sum_insert(nested_list):
                            counter = True
                            print("Day: " + str(get_day_list(nested_list)) + "  Expense: " + str(
                                get_sum_insert(nested_list)))
                            # prints appropriate lists
                    elif get_operation(params) == aux[1]:
                        # checks if relation is '<'
                        if int(params[2]) > int(get_sum_insert(nested_list)):
                            counter = True
                            print("Day: " + str(get_day_list(nested_list)) + "  Expense: " + str(
                                get_sum_insert(nested_list)))
                            # prints appropriate lists
                    elif int(params[2]) < int(get_sum_insert(nested_list)):
                        # prints appropriate lists with last relation '>'
                        counter = True
                        print(
                            "Day: " + str(get_day_list(nested_list)) + "  Expense: " + str(get_sum_insert(nested_list)))
    if ok is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist
    if counter is False:
        raise ValueError(">no sum could be printed")
    # raises error if no sum could be printed from the category


def show_category(params, content_list):
    """
    -function called by show_list function
    -prints a certain category list from the main list
    list <category> - parameters
    """
    ok = False
    # aux used to check if category exists
    for lists in content_list:
        if get_category(lists) == get_category(params):
            # searches for the right category
            ok = True
            print("Category: " + str(get_category(lists)))
            print("==========================")
            print("")
            for nested_list in lists:
                if nested_list != lists[0]:
                    print("Day: " + str(get_day_list(nested_list)) + "  Expense: " + str(get_sum_insert(nested_list)))
                    # prints the certain category list
    if ok is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist


def show_list(command_params, content_list):
    """
    -print function called by the main function
    -if parameters are empty it just prints the whole list
    -if not it calls two different functions based on parameters
    """
    if command_params is None:
        for lists in content_list:
            print("Category: " + str(get_category(lists)))
            print("==========================")
            print("")
            for nested_list in lists:
                if nested_list != lists[0]:
                    print("Day: " + str(get_day_list(nested_list)) + "  Expense: " + str(get_sum_insert(nested_list)))
            print("")
        return
        # prints the list and stops the program
    param = command_params.split(' ')
    # splits the parameters into a list of words
    params = []
    for word in param:
        if word != "":
            params.append(word)
    # gets rid of the unnecessary whitespaces in the list
    if len(params) == 1:
        show_category(params, content_list)
        # if it has one parameter it calls show_category function otherwise calls show_category_relation function
    else:
        show_category_relations(params, content_list)


def start():
    """
    -main function
    -called at the start of the program
    -calls different functions based on input
    -prints errors which have been raised
    """
    content_list = init_list()
    while True:
        command = input("prompt>")
        command_word, command_params = command_split(command)
        try:
            if command_word == 'add':
                add_to_list(command_params, content_list)
            elif command_word == 'insert':
                insert_to_list(command_params, content_list)
            elif command_word == 'remove':
                remove_list(command_params, content_list)
            elif command_word == 'list':
                show_list(command_params, content_list)
            elif command_word == 'exit':
                return
            else:
                print(">command does not exist")
        except ValueError as ve:
            print(str(ve))


start()
# test_create_add()
# test_create_insert()
