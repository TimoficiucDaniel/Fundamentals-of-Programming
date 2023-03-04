from domain.Question import Question
import random
import copy


class Gameservice:
    def __init__(self, repo, validator):
        self._repo = repo
        self._validator = validator

    def check_if_good(self, answer, question):
        """
        the function is called from the ui to check if the answer to a provided question is right or wrong and
        returns the number of points awarded according to the answer and difficulty
        :param answer:
        :param question:
        :return:
        """
        question_parameters = question.split(";")
        if answer.strip() == question_parameters[5].strip():
            if question_parameters[6].strip() == "easy":
                return 1
            elif question_parameters[6].strip() == "medium":
                return 2
            elif question_parameters[6].strip() == "hard":
                return 3
        return 0

    def add_quiz(self, parameters):
        """
        the function creates a question to add the master list with the provided parameters which are validated
        and calls a function in repo to save it in the master list and file
        :param parameters:
        :return:
        """
        function_parameters = parameters.split(";")
        self._validator.validate_add(function_parameters)
        new_question = Question(function_parameters[0], function_parameters[1], function_parameters[2],
                                function_parameters[3], function_parameters[4], function_parameters[5],
                                function_parameters[6])
        self._repo.add_question_to_file(new_question)

    def create_quiz(self, parameters):
        """
        the function takes in parameters and creates a list of questions based on the parameters which form a new quiz
        calls a function from repo to write the new quiz into a file
        :param parameters:
        :return:
        """
        function_parameters = parameters.split(" ")
        self._validator.validate_create(function_parameters)
        lungime = len(self._repo)

        if lungime < int(function_parameters[1]):
            raise ValueError(">not enough questions for this quiz")

        list_of_questions = []
        number_of_certain_questions = int(function_parameters[1]) // 2 + 1
        number_of_questions = int(function_parameters[1]) - number_of_certain_questions
        questions = copy.deepcopy(self._repo.get_questions())
        index = 0

        for question in questions:
            question_parameters = question.split(";")
            if question_parameters[6].strip() == function_parameters[0]:
                index += 1

        if index < number_of_certain_questions:
            raise ValueError(">not enough questions of that difficulty")

        while number_of_certain_questions != 0:
            index = random.randint(0, lungime - 1)
            question_parameters = questions[index].split(";")
            if question_parameters[6].strip() == function_parameters[0]:
                list_of_questions.append(questions[index])
                questions.pop(index)
                lungime -= 1
                number_of_certain_questions -= 1

        while number_of_questions != 0:
            index = random.randint(0, lungime - 1)
            list_of_questions.append(questions[index])
            questions.pop(index)
            lungime -= 1
            number_of_questions -= 1

        self._repo.create_file(list_of_questions, function_parameters[2])
