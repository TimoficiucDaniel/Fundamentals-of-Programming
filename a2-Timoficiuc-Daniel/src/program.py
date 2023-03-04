#
# Write the implementation for A2 in this file
#

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities
def show_consecutive_sum(numberlist):  # prints the longest sequence of consecutive numbers which have the same sum
    positionmax, lengthmax = find_consecutive_sum_sequence(numberlist)
    for i in range(positionmax, positionmax + lengthmax):
        print("z = " + str(get_real(numberlist[i])) + ' + ' + str(get_imag(numberlist[i])) + 'i')


def show_real_numbers(numberlist):  # prints the longest sequence of real numbers
    positionmax, lengthmax = find_real_number_sequence(numberlist)
    for i in range(positionmax, positionmax + lengthmax):
        print("z = " + str(get_real(numberlist[i])))

def add_number_ui(numberlist):  # function which takes the input which is used to add a new number to the list
    try:  # raises error to avoid crash if intput isnt a number
        real_part = float(input("Real part ="))
        imaginary_part = float(input("Imaginary part ="))
        add_number_to_list(numberlist,real_part,imaginary_part)
        print("Number added successfully!")
    except ValueError as ve:
        print(str(ve))
        return


def show_numbers(numberlist):  # prints all numbers from a list
    for lists in numberlist:
        if get_imag(lists) != 0:  # prints the only the real part if imaginary part is 0, whole number otherwise
            print("z = " + str(get_real(lists)) + ' + ' + str(get_imag(lists)) + 'i')
        else:
            print("z = " + str(get_real(lists)))


def print_menu():  # prints out the menu with the options for the different features
    print("1.Read number.")
    print("2.Show all numbers.")
    print("3.Longest sequence of real numbers.")
    print("4.Longest sequence where consecutive numbers have equal sum.")
    print("5.Exit.")


def start():  # starts the function
    numberlist = init_numbers()
    while True:
        print_menu()  # prints menu
        option = input("User option =")  # options for the features
        if option == '1':
            add_number_ui(numberlist)
        elif option == '2':
            show_numbers(numberlist)
        elif option == '3':
            show_real_numbers(numberlist)
        elif option == '4':
            show_consecutive_sum(numberlist)
        elif option == '5':
            return
        else:
            print("Invalid input.")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values
def find_consecutive_sum_sequence(numberlist):  # finds the longest sequence of consecutive numbers with equal sums
    sum_list = []
    obtain_sum(numberlist, sum_list)  # we create a list which contains the sum of all consecutive numbers from the list
    lengthmax = 0
    positionmax = 0
    position = 0
    length = 0
    count = 0
    while count < len(sum_list) - 1:  # we go through the list comparing the sums
        if sum_list[count] == sum_list[count + 1]:  # if the sums are equal we increase the length of the sequence and set the position
            if length == 0:
                position = count*2
                length=2
            length += 2
        else:
            if length > lengthmax:  # otherwise we compare the length to the maxlength and replace them accordingly
                lengthmax = length
                positionmax = position
            length = 0
        count += 1
    if length > lengthmax:  # final test
        lengthmax = length
        positionmax = position
    return positionmax, lengthmax  # return the start position of the sequence in the original list and its length


def find_real_number_sequence(numberlist): # function that finds the longest sequence of real numbers
    lengthmax = 0
    positionmax = 0
    count = 0
    length = 0
    for lists in numberlist: #we go through the list and check if its a real number
        if get_imag(lists) == 0: # if it is we increase the length and set the position in the original list
            if length == 0:
                position = count
            length += 1

        else:
            if length > lengthmax: # otherwise we compare
                lengthmax = length
                positionmax = position
            length = 0
        count += 1
    if length > lengthmax: #final test
        lengthmax = length
        positionmax = position
    return positionmax, lengthmax # return the start position of the sequence in the original list and its length


def init_numbers(): #intialize some numbers
    return [create_number(1, 2), create_number(2, 3), create_number(3, 2), create_number(1, 1), create_number(1, 1),
            create_number(1, 1), create_number(1, 1), create_number(1, 1), create_number(1, 1), create_number(1, 1)]


def create_number(real_part, imaginary_part): # create a list containing the parts of the number
    return [real_part,imaginary_part]


def get_real(number): # get real part
    return number[0]


def get_imag(number): # get imaginary part
    return number[1]


def add_number(number, numberlist): # add number to list
    numberlist.append(number)


def obtain_sum(numberlist, sum_list): # construct the list of the sums of consecutive numbers
    for i in range(0,len(numberlist) ,2):
        real = get_real(numberlist[i]) + get_real(numberlist[i + 1])
        imag = get_imag(numberlist[i]) + get_imag(numberlist[i + 1])
        number = create_number(real, imag)
        #print(number)
        sum_list.append(number)

def add_number_to_list(numberlist,real_part,imaginary_part):
    number = create_number(real_part, imaginary_part)
    add_number(number, numberlist)


start()
