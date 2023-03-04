class Ui:
    def __init__(self, game_service, repo):
        self._game_service = game_service
        self._repo = repo

    def start_game(self, file_name):
        self._repo.load_certain_file(file_name)
        score = 0
        for questions in self._repo.get_questions():
            question_specifications = questions.split(";")
            print(str(question_specifications[0]) + ";" + str(question_specifications[1]) + ";" + str(
                question_specifications[2]) + ";" + str(question_specifications[3]) + ";" \
                  + str(question_specifications[4]) + ";" + str(question_specifications[6]))
            answer = input("Your choice?")
            score += self._game_service.check_if_good(answer, questions)
        print("Your score is =" + str(score))
        self._repo.load_file()

    def start_program(self):
        while True:
            try:
                print("Options:")
                print("add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty>")
                print("create <difficulty> <number_of_questions> <file>")
                print("start <file>")
                print("exit code")
                option = input("Input>")
                command, parameters = option.split(" ", maxsplit=1)
                if command.strip() == "add":
                    self._game_service.add_quiz(parameters)
                elif command.strip() == "create":
                    self._game_service.create_quiz(parameters)
                elif command.strip() == "start":
                    self.start_game(parameters)
                elif command.strip() == "exit":
                    return
                else:
                    print("invalid input")
            except ValueError as ve:
                print(str(ve))
