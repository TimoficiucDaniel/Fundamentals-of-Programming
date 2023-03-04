import getters


def check_error_show_sum_category(params, content_list):
    if len(params) != 1:
        raise ValueError(">incorrect parameters")
    ok = False
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            ok = True
    if ok is False:
        raise ValueError(">category does not exist")


def check_if_empty(command_params):
    if command_params is None:
        raise ValueError(">parameters not specified")
    # raises error if parameters are empty


def check_error_add_to_list(params):
    if len(params) != 2:
        raise ValueError(">incorrect parameters")
    # raises error if there are too many or too few parameters
    x = getters.get_sum_add(params)
    if x.isnumeric() is False:
        raise ValueError(">sum has to be an integer")
    # raises error if sum parameter is not an integer


def check_error_show_category_relations(params):
    aux = ["=", "<", ">"]
    # list containing the three possible relations
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
    # raises error if too many or too few parameters
    if getters.get_operation(params) not in aux:
        raise ValueError(">incorrect operation")
    # raises error if the relation parameter is not in the relation list
    if getters.get_sum_show_category(params).isnumeric() is False:
        raise ValueError(">sum has to be an integer")
    # raises error if the sum parameter is not an integer


def check_error_remove_days(params):
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
        # checks for appropriate number of parameters,raises error if not
        # enough or too many parameters
    if getters.get_operation(params) != "to":
        raise ValueError(">invalid operation")
        # checks if the second parameter is the word "to", raises error if not"to"
    if int(getters.get_day_list(params)) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
        # checks if the day1 parameter is from [1,30],raises
        # error otherwise
    if int(getters.get_day2(params)) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
        # checks if the day2 parameter is from [1,30],raises
        # error otherwise
    if int(getters.get_day_list(params)) == int(getters.get_day2(params)) or abs(
            int(getters.get_day2(params)) - int(getters.get_day_list(params))) == 1:
        # checks if the days are equal ore are consecutive,
        # raises error if so since we remove the days fromm the interval (day1,day2)
        raise ValueError(">days cannot be the same or consecutive")


def check_error_remove_day(params):
    x = getters.get_day_list(params)
    if int(x) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
        # checks if day param is in the correct interval
        # raises error if not


def check_error_insert_to_list(params):
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
    # raises error if there are too many or too few parameters
    x = getters.get_sum_insert(params)
    if x.isnumeric() is False:
        raise ValueError(">sum has to be an integer")
    # raises error if sum parameter is not an integer
    y = getters.get_day_insert(params)
    if y.isnumeric() is False:
        raise ValueError(">day has to be an integer")
    # raises error if day parameter is not an integer
    if int(y) not in range(1, 31):
        raise ValueError(">day has to be from the interval [1,30]")
    # raises error if day parameter is not in the correct interval


def check_error_find_max(params):
    if len(params) != 1:
        raise ValueError(">incorrect parameters")
    if getters.get_day_list(params) != 'day':
        raise ValueError(">command does not exist")


def check_error_sort_day(params):
    if len(params) != 1:
        raise ValueError(">incorrect parameters")


def check_error_sort_day_category(params, content_list):
    ok = False
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            ok = True
    if ok is False:
        raise ValueError(">category does not exist")


def check_if_empty_undo(command_params):
    if command_params is not None:
        raise ValueError(">command does not exist")
    # raises error if parameters are empty


def check_error_filter(params, content_list):
    ok = False
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            ok = True
    if ok is False:
        raise ValueError(">category does not exist")


def check_error_filter_operation(params):
    if len(params) != 3:
        raise ValueError(">incorrect parameters")
    aux = ["=", "<", ">"]
    if getters.get_operation(params) not in aux:
        raise ValueError(">incorrect operation")
    if getters.get_sum_show_category(params).isnumeric() is False:
        raise ValueError(">sum has to be an integer")
