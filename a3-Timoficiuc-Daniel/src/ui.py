import getters
import validate_functions


def print_list(content_list):
    for lists in content_list:
        print("Category: " + str(getters.get_category(lists)))
        print("==========================")
        print("")
        for nested_list in lists:
            if nested_list != getters.get_category(lists) and len(nested_list) > 1:
                print("Day: " + str(getters.get_day_list(nested_list)) + "  Expense: " + str(
                    getters.get_sum_insert(nested_list)))
        print("")
    # prints the list


def show_category(params, content_list):
    """
    -function called by show_list function
    -prints a certain category list from the main list
    list <category> - parameters
    """
    ok = False
    # aux used to check if category exists
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            # searches for the right category
            ok = True
            print("Category: " + str(getters.get_category(lists)))
            print("==========================")
            print("")
            for nested_list in lists:
                if nested_list != getters.get_category(lists) and len(nested_list) > 1:
                    print("Day: " + str(getters.get_day_list(nested_list)) + "  Expense: " + str(
                        getters.get_sum_insert(nested_list)))
                    # prints the certain category list
    if ok is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist


def show_category_relations(params, content_list):
    """
    -function called by the show_list function
    -prints all items from a category list with a certain relation to the input
    list <category> [ < | = | > ] <value> - parameters
    -relations can be =,<,>
    """
    aux = ["=", "<", ">"]
    validate_functions.check_error_show_category_relations(params)
    # list containing the three possible relations
    ok = False
    # aux used to check if category exists
    counter = False
    # aux used to check if there are any lists that could be printed
    for lists in content_list:
        if getters.get_category(lists) == getters.get_category(params):
            ok = True
            print("Category: " + str(getters.get_category(lists)))
            print("==========================")
            print("")
            for nested_list in lists:
                if nested_list != getters.get_category(lists) and len(nested_list) > 1:
                    if getters.get_operation(params) == aux[0]:
                        # checks if relation is '='
                        if int(getters.get_sum_show_category(params)) == getters.get_sum_insert(nested_list):
                            counter = True
                            print("Day: " + str(getters.get_day_list(nested_list)) + "  Expense: " + str(
                                getters.get_sum_insert(nested_list)))
                            # prints appropriate lists
                    elif getters.get_operation(params) == aux[1]:
                        # checks if relation is '<'
                        if int(getters.get_sum_show_category(params)) > int(getters.get_sum_insert(nested_list)):
                            counter = True
                            print("Day: " + str(getters.get_day_list(nested_list)) + "  Expense: " + str(
                                getters.get_sum_insert(nested_list)))
                            # prints appropriate lists
                    elif int(getters.get_sum_show_category(params)) < int(getters.get_sum_insert(nested_list)):
                        # prints appropriate lists with last relation '>'
                        counter = True
                        print(
                            "Day: " + str(getters.get_day_list(nested_list)) + "  Expense: " + str(
                                getters.get_sum_insert(nested_list)))
    if ok is False:
        raise ValueError(">category does not exist")
    # raises error if category does not exist
    if counter is False:
        raise ValueError(">no sum could be printed")
    # raises error if no sum could be printed from the category


def print_sum(params, sum):
    print(str(getters.get_category(params)) + " Total Sum = " + str(sum))


def print_max_day(max, position):
    print("Maximum expenses out of all days are for day : " + str(position + 1) + " with a sum of : " + str(max))


def print_sorted_days(sorted_list):
    for lists in sorted_list:
        if getters.get_sum(lists) != 0:
            print("Day : " + str(getters.get_day_list(lists)) + " Total daily expense : " + str(getters.get_sum(lists)))


def print_day_category(lists, new_list):
    print("Category: " + str(getters.get_category(lists)))
    print("==========================")
    print("")
    for nested_list in new_list:
        print("Day: " + str(getters.get_day_list(nested_list)) + "  Expense: " + str(
            getters.get_sum_insert(nested_list)))
