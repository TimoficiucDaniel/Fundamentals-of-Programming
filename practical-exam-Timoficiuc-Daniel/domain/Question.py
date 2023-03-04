class Question:
    def __init__(self, id, text, choice_a, choice_b, choice_c, correct, difficulty):
        self._id = id
        self._text = text
        self._choice_a = choice_a
        self._choice_b = choice_b
        self._choice_c = choice_c
        self._correct = correct
        self._difficulty = difficulty

    def __repr__(self):
        return str(self._id) + ";" + str(self._text) + ";" + str(self._choice_a) + ";" + str(self._choice_b) + ";" \
               + str(self._choice_c) + ";" + str(self._correct) + ";" + str(self._difficulty)

    def __str__(self):
        return str(self._id) + ";" + str(self._text) + ";" + str(self._choice_a) + ";" + str(self._choice_b) + ";" \
               + str(self._choice_c) + ";" + str(self._correct) + ";" + str(self._difficulty)
