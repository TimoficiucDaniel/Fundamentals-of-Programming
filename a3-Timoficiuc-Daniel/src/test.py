import functions
import getters


def test_remove_function(params, lists):
    functions.remove_list(params, lists)
    return lists


def test_swap_days():
    day1 = 1
    day2 = 2
    day1, day2 = functions.swap_days(day1, day2)
    assert day1 == 2
    assert day2 == 1


def test_remove_list():
    try:
        functions.remove_list(None, [])
    except ValueError as ve:
        assert str(ve) == ">parameters not specified"
    try:
        functions.remove_list('1 2 3 4', [])
    except ValueError as ve:
        assert str(ve) == ">incorrect parameters"
    try:
        functions.remove_list('1 2 4', [])
    except ValueError as ve:
        assert str(ve) == ">invalid operation"
    try:
        functions.remove_list('1 to 34', [])
    except ValueError as ve:
        assert str(ve) == ">day has to be from the interval [1,30]"
    try:
        functions.remove_list('155 to 5', [])
    except ValueError as ve:
        assert str(ve) == ">day has to be from the interval [1,30]"
    try:
        functions.remove_list('5 to 5', [])
    except ValueError as ve:
        assert str(ve) == ">days cannot be the same or consecutive"
    try:
        functions.remove_list('4 to 5', [])
    except ValueError as ve:
        assert str(ve) == ">days cannot be the same or consecutive"
    content_list = [['food', [1, 50], [5, 60], [7, 50]]]
    assert test_remove_function('3 to 6', content_list) == [['food', [1, 50], [7, 50]]]
    try:
        functions.remove_list('35', [])
    except ValueError as ve:
        assert str(ve) == ">day has to be from the interval [1,30]"
    test_list = [['food', [1, 50], [2, 50]]]
    assert test_remove_function('1', test_list) == [['food', [2, 50]]]
    test_list2 = [['housekeeping', [4, 50]], ['food', [6, 50]]]
    assert test_remove_function('food', test_list2) == [['housekeeping', [4, 50]], ['food']]


def test_split_params():
    command_params = 'one and two'
    assert functions.split_params(command_params) == ['one', 'and', 'two']


def test_create_list_insert():
    params = ['one', 'two']
    assert functions.create_list_insert(params) == ['one', 'two']


def test_insert(params, list):
    functions.insert_to_list(params, list)
    return list


def test_insert_to_list():
    try:
        functions.insert_to_list(None, [])
    except ValueError as ve:
        assert str(ve) == ">parameters not specified"
    try:
        functions.insert_to_list('1 2', [])
    except ValueError as ve:
        assert str(ve) == ">incorrect parameters"
    try:
        functions.insert_to_list('sd 50 food', [])
    except ValueError as ve:
        assert str(ve) == ">day has to be an integer"
    try:
        functions.insert_to_list('21 asd food', [])
    except ValueError as ve:
        assert str(ve) == ">sum has to be an integer"
    try:
        functions.insert_to_list('41 50 food', [])
    except ValueError as ve:
        assert str(ve) == ">day has to be from the interval [1,30]"
    test_list = [['food']]
    assert test_insert('20 50 food', test_list) == [['food', ['20', '50']]]


def test_create_list_add():
    assert functions.create_list_add([11]) == [5, 11]


def test_add(params, list):
    functions.add_to_list(params, list)
    return list


def test_add_to_list():
    try:
        functions.add_to_list(None, [])
    except ValueError as ve:
        assert str(ve) == ">parameters not specified"
    try:
        functions.add_to_list('1 2 3', [])
    except ValueError as ve:
        assert str(ve) == ">incorrect parameters"
    try:
        functions.add_to_list('asd food', [])
    except ValueError as ve:
        assert str(ve) == ">sum has to be an integer"
    test_list = [['food']]
    assert test_add('10 food', test_list) == [['food', [5, '10']]]


def test_calculate_days():
    test_list = [["housekeeping", [20, 25], [16, 29]], ["food", [20, 250], [1, 300]], ["transport", [12, 34], [4, 2]],
                 ["clothing", [4, 30], [16, 500], [5, 25]], ["internet", [18, 90]], ["others", [18, 200]]]
    assert functions.calculate_days(test_list) == [300, 0, 0, 32, 25, 0, 0, 0, 0, 0, 0, 34, 0, 0,
                                                   0, 529, 0, 290, 0, 275, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_sorting():
    test_list = [[1, 3], [5, 5], [6, 7], [30, 6], [2, 4], [5, 1]]
    assert functions.sorting(test_list) == [[5, 1], [1, 3], [2, 4], [5, 5], [30, 6], [6, 7]]


def test_all():
    test_swap_days()
    test_remove_list()
    test_split_params()
    test_create_list_insert()
    test_insert_to_list()
    test_create_list_add()
    test_add_to_list()
    test_calculate_days()
    test_sorting()


test_all()
