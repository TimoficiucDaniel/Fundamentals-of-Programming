import random


class expense:
    def __init__(self, day, amount, type):
        validate_expense(day, amount)
        self._day = day
        self._amount = amount
        self._type = type

    @property
    def amount(self):
        return self._amount

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Day : " + str(self._day) + " Amount : " + str(self._amount) + " Type : " + str(self._type)


def validate_expense(day, amount):
    if str(day).isnumeric() is False:
        raise ValueError("day has to be an integer")
    if int(day) not in range(1, 31):
        raise ValueError("day has to be in interval [1,30]")
    if str(amount).isnumeric() is False:
        raise ValueError("amount has to be an integer")


def generate_expenses(n=10):
    type_list = ["food", "clothing", "bills", "car extended warranty", "internet", "snacks", "others"]
    expense_list = []
    while n > 0:
        random_day = random.randint(1, 30)
        random_amount = random.randint(10, 300)
        random_type = random.randint(0, 6)
        generated_expense = expense(random_day, random_amount, type_list[random_type])
        expense_list.append(generated_expense)
        n -= 1
    return expense_list
