from services import functions
from domain import expense
import copy


def test_expenses():
    test_ex = expense.expense(10, 20, 'food')
    assert test_ex.amount == 20
    try:
        ex_fail1 = expense.expense(40, 20, 'food')
    except ValueError as ve:
        assert str(ve) == "day has to be in interval [1,30]"
    try:
        ex_fail2 = expense.expense('idk', 20, 'food')
    except ValueError as ve:
        assert str(ve) == "day has to be an integer"
    try:
        ex_fail2 = expense.expense(20, 'idk', 'food')
    except ValueError as ve:
        assert str(ve) == "amount has to be an integer"


def test_split_parameters():
    var1, var2, var3 = functions.split_parameters("I   like   turtles")
    assert var1 == "I"
    assert var2 == "like"
    assert var3 == "turtles"
    try:
        var1, var2, var3 = functions.split_parameters("I dont like turtles")
    except ValueError as ve:
        assert str(ve) == "incorrect parameters"


def test_add_to_list():
    test_func = functions.functions()
    test_list = test_func.expense_list.copy()
    test_func.add_to_list('10 20 food')
    test_list.append(test_func.expense_list[10])
    assert test_func.expense_list == test_list


def test_filter_list():
    test_func = functions.functions()
    var1 = expense.expense(10, 200, 'food')
    var2 = expense.expense(10, 210, 'food')
    test_func._expense_list = [var1, var2].copy()
    test_func.filter_list('205')
    assert test_func.expense_list == [var2]


def test_all():
    test_expenses()
    test_split_parameters()
    test_add_to_list()
    test_filter_list()


test_all()
