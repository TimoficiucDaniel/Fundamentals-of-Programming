from domain import expense
import copy


class functions:
    def __init__(self):
        self._expense_list = expense.generate_expenses()
        self._undo_list = []
        self._undo_list.append(copy.deepcopy(self._expense_list))

    def add_to_list(self, string):
        day, amount, type = split_parameters(string)
        new_expense = expense.expense(day, amount, type)
        self._expense_list.append(new_expense)
        self._undo_list.append(copy.deepcopy(self._expense_list))

    def filter_list(self, string):
        filter_amount = string.strip(" ")
        check_filter_amount(filter_amount)
        for expenses in list(self._expense_list):
            if int(expenses.amount) < int(filter_amount):
                self._expense_list.remove(expenses)
        self._undo_list.append(copy.deepcopy(self._expense_list))

    def undo_list(self):
        if len(self._undo_list) > 1:
            self._undo_list.pop(-1)
            self._expense_list = copy.deepcopy(self._undo_list[-1])
        else:
            raise ValueError("no operations to undo")

    @property
    def expense_list(self):
        return self._expense_list


def split_parameters(string):
    parameters = string.split(' ')
    new_parameters = []
    for words in parameters:
        if words != "":
            new_parameters.append(words)
    if len(new_parameters) != 3:
        raise ValueError("incorrect parameters")
    return new_parameters[0], new_parameters[1], new_parameters[2]


def check_filter_amount(filter_amount):
    if str(filter_amount).isnumeric() is False:
        raise ValueError("amount that you filter by has to be an integer")

