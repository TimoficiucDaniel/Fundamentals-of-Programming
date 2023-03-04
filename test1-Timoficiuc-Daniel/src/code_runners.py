"""
Implement the solution here. 
You may add other source files.
Make sure you commit & push the source code before the end of the test.

Solutions using user-defined classes will not be graded.
"""
"""non-ui"""
import random
import time


def generate_number():
    # randint is used to generate random good integer
    x = random.randint(1, 9)
    aux = True
    while aux is True:
        y = random.randint(0, 9)
        if y != x:
            aux = False
    aux = True
    while aux is True:
        z = random.randint(0, 9)
        if z != x and z != y:
            aux = False
    aux = True
    while aux is True:
        t = random.randint(0, 9)
        if t != x and t != y and t != z:
            aux = False
    number = str(x) + str(y) + str(z) + str(t)
    return number


def validate_guess(guess):
    if str(guess).isnumeric() is False:
        raise ValueError(">guess has to be a number")
    if len(guess) != 4:
        raise ValueError(">guess has to be a 4 digit number")
    if int(guess) == 8086:
        return
    lists = list(guess)
    if lists[0] == '0':
        raise ValueError(">guess cannot start with 0")
    for i in range(4):
        for j in range(4):
            if i != j:
                if lists[i] == lists[j]:
                    raise ValueError(">incorrect format for guess")


def check_guess(guess, number):
    if int(guess) == 8086:
        cheat_print(number)
        return True
    if int(guess) == int(number):
        player_won(number)
        return False
    c = 0
    r = 0
    list1 = list(number)
    list2 = list(guess)
    for i in range(4):
        for j in range(4):
            if list1[i] == list2[j]:
                if i == j:
                    c += 1
                else:
                    r += 1
    print_hints(c, r)
    return True


"""UI"""


def cheat_print(number):
    print("Secret number is : " + str(number))


def player_won(number):
    print("You guessed the number correctly and it was: " + str(number))


def print_hints(c, r):
    print(str(c) + " codes and " + str(r) + " runners")


def start():
    number = generate_number()
    aux = True
    a = time.time()
    while aux is True:
        try:
            guess = input("Your guess=? ")
            b = time.time()
            if b - a > 60:
                print("Time is up! Computer won!")
                return
            guess = guess.strip()
            validate_guess(guess)
            aux = check_guess(guess, number)
        except ValueError as ve:
            print(str(ve))
            print("Computer won!")
            return


start()
