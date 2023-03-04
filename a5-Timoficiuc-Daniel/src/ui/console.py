from services import functions


class ui:
    def __init__(self):
        self._func = functions.functions()

    def print_expenses(self):
        counter = 1
        for expenses in self._func.expense_list:
            print(str(counter) + ". " + str(expenses))
            counter += 1

    @staticmethod
    def show_menu():
        print("1.Add expense.")
        print("2.Display expenses.")
        print("3.Filter expenses based on amount.")
        print("4.Undo.")
        print("5.Exit.")

    def start(self):
        while True:
            self.show_menu()
            option = input("Input = ")
            option=option.strip(" ")
            try:
                if option == '1':
                    string = input("Insert expense: ")
                    self._func.add_to_list(string)
                    print("Expense added successfully!")
                elif option == '2':
                    self.print_expenses()
                elif option == '3':
                    string = input("Insert amount to filter by: ")
                    self._func.filter_list(string)
                    print("Filtered successfully!")
                elif option == '4':
                    self._func.undo_list()
                    print("Undo was performed successfully!")
                elif option == '5':
                    return
                else:
                    print("Incorrect input.")
            except ValueError as ve:
                print(str(ve))


ui_start = ui()
ui_start.start()
