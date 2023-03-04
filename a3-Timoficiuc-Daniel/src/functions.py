import validate_functions
import ui
import getters
from datetime import date
import copy


def swap_days(day1, day2):
    return day2, day1
    # swaps day1 day2 parameters around if day2 < day1


def remove_category(params, content_list):
    """
    -function called by the remove_list function
    -removes all elements from a list corresponding to the specified category
    remove <category> -parameters
    """
    counter = False
    # aux used to check if category exists
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            counter = True
            x = getters.get_category(params)
            lists.clear()
            lists.append(x)
            # function remembers the first element of the list which is always the category then
            # clears the list and inserts the category back into the first spot in the list
    if counter is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist


def remove_day(params, content_list):
    """
    -function called by the remove_list function
    -removes all items from the main list whose day param is equal to a certain day from input
    -checks for errors
    remove <day> -parameters
    """
    validate_functions.check_error_remove_day(params)
    ok = False
    # aux to check if the certain day appears anywhere in the list
    for lists in content_list:
        counter1 = 0
        counter2 = 0
        for nested_list in list(lists):
            # list(lists) creates a copy of lists which we iterate so that when we pop items
            # we do not have problems with iteration
            if str(getters.get_day_list(params)) == str(getters.get_day_list(nested_list)):
                ok = True
                lists.pop(counter1)
                counter1 -= 1
                # pops the certain item [day,sum] from the list whose day param is equal to the specified one
            counter1 += 1
            counter2 += 1
    if ok is False:
        raise ValueError(">day does not appear anywhere")
        # raises error if no days were removed


def remove_days(params, content_list):
    """
    -this function is called by the main remove_list function
    -checks for input errors such as number of param, type etc
    -removes items from the main list whose day param is between day1,day2 parameters of this function
    remove <start day> to <end day> -parameters
    """
    validate_functions.check_error_remove_days(params)
    if int(getters.get_day2(params)) < int(getters.get_day_list(params)):
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
            if str(getters.get_day_list(nested_list)).isnumeric() is True:
                if int(getters.get_day_list(params)) < int(getters.get_day_list(nested_list)) < int(
                        getters.get_day2(params)):
                    ok = True
                    lists.pop(counter)
                    counter -= 1
                    # if the day is in the interval we pop the list [day,sum] from the main list and decrement
                    # counter by 1 to match the shift of indexes
            counter += 1
    if ok is False:
        raise ValueError(">day does not appear anywhere")
        # raise error if no days were removed


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
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    if len(params) > 1:
        # if the function has multiple parameters it calls the remove_days function
        remove_days(params, content_list)
    elif getters.get_sum_add(params).isnumeric() is True:
        # if the function parameter is numeric it calls the remove_day function
        remove_day(params, content_list)
    else:
        remove_category(params, content_list)
        # if none of the other are true it calls the remove category function


def show_list(command_params, content_list):
    """
    -print function called by the main function
    -if parameters are empty it just prints the whole list
    -if not it calls two different functions based on parameters
    """
    if command_params is None:
        ui.print_list(content_list)
        return
    params = split_params(command_params)
    if len(params) == 1:
        ui.show_category(params, content_list)
        # if it has one parameter it calls show_category function otherwise calls show_category_relation function
    else:
        ui.show_category_relations(params, content_list)


def split_params(command_params):
    param = command_params.split(' ')
    # splits the command parameters into a list of words
    params = []
    for word in param:
        if word != "":
            params.append(word)
            # function that removes the whitespaces that happen to be interpreted as words
    return params


def create_list_insert(params):
    """
    -called by the insert_to_list function
    -returns a list composed of day and sum parameters
    """
    aux = []
    aux.append(getters.get_day_insert(params))
    aux.append(getters.get_sum_insert(params))
    return aux


def insert_to_list(command_params, content_list):
    """
    -function that inserts a sum at a certain day into a certain category in the main list
    -checks for input errors
    -insert <day> <sum> <category> -parameters
    """
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    validate_functions.check_error_insert_to_list(params)
    ok = False
    # aux used to check if category appears in the list
    for lists in content_list:
        if getters.get_category_insert(params) == getters.get_category(lists):
            ok = True
            aux = create_list_insert(params)
            # calls a function that creates the specified [day,sum] list
            lists.append(aux)
            # appends list to the specified category in the main list
    if ok is False:
        raise ValueError(">category does not exist")
    # raises error if the category does not exist


def create_list_add(params):
    """
    -function called by the add_to_list function
    -returns a list composed of the current date day and the sum
    -current date day is obtained using .today() function from the datetime module
    """
    aux = []
    today = date.today()
    aux.append(today.day)
    aux.append(getters.get_sum_add(params))
    return aux


def add_to_list(command_params, content_list):
    """
    -function which adds a sum to a category using the current date from the calendar
    -checks for input errors
    add <sum> <category> -parameters
    """
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    validate_functions.check_error_add_to_list(params)
    aux = create_list_add(params)
    # calls a function which creates the desired list of the form [current_date.day,sum]
    counter = False
    # aux used to check if category appears in the main list
    for lists in content_list:
        if getters.get_category_add(params) == getters.get_category(lists):
            counter = True
            lists.append(aux)
            # appends the [day,sum] list to the category list
    if counter is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist


def show_sum_category(command_params, content_list):
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    validate_functions.check_error_show_sum_category(params, content_list)
    sum = 0
    for lists in content_list:
        if getters.get_category(params) == getters.get_category(lists):
            for nested_list in lists:
                if nested_list != getters.get_category(lists):
                    sum = sum + int(getters.get_sum(nested_list))
    ui.print_sum(params, sum)


def calculate_days(content_list):
    days = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for lists in content_list:
        for nested_list in lists:
            if nested_list != getters.get_category(lists):
                days[getters.get_day_list(nested_list) - 1] = days[getters.get_day_list(
                    nested_list) - 1] + getters.get_sum(nested_list)
    return days


def find_max(command_params, content_list):
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    validate_functions.check_error_find_max(params)
    days = calculate_days(content_list)
    max = -1
    position = -1
    for poz in range(0, 30):
        if days[poz] > max:
            position = poz
            max = days[poz]
    ui.print_max_day(max, position)


def create_list_day_sum(day, sum):
    return [day, sum]


def create_list_sort_day(days):
    sorted_list = []
    for i in range(0, 30):
        nested_list = create_list_day_sum(i + 1, days[i])
        sorted_list.append(nested_list)
    return sorted_list


def sorting(list):
    list.sort(key=lambda x: x[1])
    return list


def sort_day(command_params, content_list):
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    validate_functions.check_error_sort_day(params)
    if getters.get_category(params) == 'day':
        days = calculate_days(content_list)
        sorted_list = create_list_sort_day(days)
        sorted_list = sorting(sorted_list)
        ui.print_sorted_days(sorted_list)
    else:
        sort_day_category(params, content_list)


def create_category_list(lists):
    new_list = lists.copy()
    new_list.pop(0)
    return new_list


def sort_day_category(params, content_list):
    validate_functions.check_error_sort_day_category(params, content_list)
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            new_list = create_category_list(lists)
            new_list = sorting(new_list)
            ui.print_day_category(params, new_list)


def undo_list(command_params, content_list, undo_list):
    validate_functions.check_if_empty_undo(command_params)
    if len(undo_list) > 1:
        undo_list.pop(-1)
        content_list = copy.deepcopy(undo_list[-1])
    else:
        raise ValueError(">no operations to undo")
    return content_list


def filter(command_params, content_list):
    validate_functions.check_if_empty(command_params)
    params = split_params(command_params)
    validate_functions.check_error_filter(params, content_list)
    if len(params) == 1:
        filter_category(params, content_list)
    else:
        filter_operation(params, content_list)


def filter_category(params, content_list):
    for lists in content_list:
        if getters.get_category(lists) != getters.get_category(params):
            x = getters.get_category(lists)
            lists.clear()
            lists.append(x)


def filter_operation(params, content_list):
    validate_functions.check_error_filter_operation(params)
    for lists in content_list:
        counter = 0
        if getters.get_category(lists) == getters.get_category(params):
            for nested_list in lists:
                if nested_list != getters.get_category(lists):
                    if getters.get_operation(params) == '=':
                        if int(getters.get_sum_show_category(params)) != getters.get_sum(nested_list):
                            nested_list.pop(counter)
                    if getters.get_operation(params) == '>':
                        if int(getters.get_sum_show_category(params)) > getters.get_sum(nested_list):
                            nested_list.pop(counter)
                    if getters.get_operation(params) == '<':
                        if int(getters.get_sum_show_category(params)) < getters.get_sum(nested_list):
                            nested_list.pop(counter)
            counter += 1
