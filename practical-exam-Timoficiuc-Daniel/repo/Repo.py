class Repository:
    def __init__(self, file_name):
        self._file_name = file_name
        self._quizes = None

    def get_questions(self):
        """
        return the master list of questions
        :return:
        """
        return self._quizes

    def __len__(self):
        """
        returns the length of the master list
        :return:
        """
        return len(self._quizes)

    def load_file(self):
        """
        loads the initial file and reads and store the master list
        :return:
        """
        f = open(self._file_name,"rt")
        self._quizes = []
        for lines in f.readlines():
            if lines != "\n":
                self._quizes.append(lines)
        f.close()

    def load_certain_file(self,file_name):
        """
        called to load a certain file for the main game from which questions are extracted
        :param file_name:
        :return:
        """
        f = open(file_name, "rt")
        self._quizes = []
        for lines in f.readlines():
            if lines != "\n":
                self._quizes.append(lines)
        f.close()

    def create_file(self,list_of_questions,file_name):
        """
        takes in a list of questions which represent a quiz and writes it into a specified file
        :param list_of_questions:
        :param file_name:
        :return:
        """
        f = open(file_name,"wt")
        for questions in list_of_questions:
            f.write(questions+"\n")
        f.close()

    def add_question_to_file(self,question):
        """
        adds a question to the master list and to the file
        :param question:
        :return:
        """
        self._quizes.append(str(question))
        f = open(self._file_name,"wt")
        for lines in self._quizes:
            f.write(lines+"\n")
        f.close()


class Validator:
    def __init__(self):
        pass

    def validate_add(self, parameters):
        """
        validates the parameters for the add function
        :param parameters:
        :return:
        """
        difficulties = ["easy", "medium", "hard"]
        if len(parameters) != 7:
            raise ValueError(">incorrect amount of parameters")
        if str(parameters[0]).isnumeric() is False:
            raise ValueError(">id has to be an integer")
        if parameters[6] not in difficulties:
            raise ValueError(">incorrect difficulty")
        if parameters[5] != parameters[2] and parameters[5] != parameters[3] and parameters[5] != parameters[4]:
            raise ValueError(">correct choice doesnt match any of the given choices")

    def validate_create(self,parameters):
        """
        validates the parameters for the create function
        :param parameters:
        :return:
        """
        difficulties = ["easy", "medium", "hard"]
        if len(parameters) != 3:
            raise ValueError(">incorrect number of parameters")
        if parameters[0] not in difficulties:
            raise ValueError(">incorrect difficulty")
        if str(parameters[1]).isnumeric() is False:
            raise ValueError(">incorrect format for number of questions")