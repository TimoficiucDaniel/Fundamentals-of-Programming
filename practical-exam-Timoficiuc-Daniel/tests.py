import unittest
from repo.Repo import Repository
from domain.Question import Question
from service.GameService import Gameservice
from repo.Repo import Validator


class TestRepo(unittest.TestCase):
    def setUp(self):
        self.repo = Repository("myquiz2.txt")

    def test_load_file(self):
        self.repo.load_file()
        self.assertEqual(self.repo.get_questions(), ['1;Which number is the largest;1;4;3;4;easy\n',
                                                     '2;Which number is the smallest;-3;3;0;-3;easy\n',
                                                     '3;Which number is prime;2;32;9;2;easy\n',
                                                     '4;Which country has the largest GDP;Brazil;China;UK;China;medium\n',
                                                     '5;Which is not a fish;carp;orca;eel;orca;medium\n',
                                                     '6;Name the first satellite;Apollo;Sputnik;Zaria;Sputnik;medium\n',
                                                     '7;Which Apollo mission did not make it to the moon;11;13;17;13;hard\n',
                                                     '8;A mole can be;animal;quantity;both;both;hard\n',
                                                     "9;Name El Cid's horse;Babieca;Abu;Santiago;Babieca;hard\n",
                                                     '10;The Western Roman Emprire fell in;654;546;476;476;hard\n',
                                                     '1;1;1;2;3;1;easy\n',
                                                     '1;1;1;2;3;1;easy\n'])

    def test_load_certain_file(self):
        self.repo.load_certain_file("myquiz.txt")
        self.assertEqual(self.repo.get_questions(), ['1;Which number is the largest;1;4;3;4;easy\n',
                                                     '2;Which number is the smallest;-3;3;0;-3;easy\n',
                                                     '3;Which number is prime;2;32;9;2;easy\n',
                                                     '4;Which country has the largest GDP;Brazil;China;UK;China;medium\n',
                                                     '5;Which is not a fish;carp;orca;eel;orca;medium\n',
                                                     '6;Name the first satellite;Apollo;Sputnik;Zaria;Sputnik;medium\n',
                                                     '7;Which Apollo mission did not make it to the moon;11;13;17;13;hard\n',
                                                     '8;A mole can be;animal;quantity;both;both;hard\n',
                                                     "9;Name El Cid's horse;Babieca;Abu;Santiago;Babieca;hard\n",
                                                     '10;The Western Roman Emprire fell in;654;546;476;476;hard\n'])

    def test__len__(self):
        self.repo.load_certain_file("myquiz.txt")
        self.assertEqual(len(self.repo.get_questions()), 10)

    def test_create_file(self):
        self.repo.create_file(["idk"], "test.txt")
        self.repo.load_certain_file("test.txt")
        self.assertEqual(self.repo.get_questions(), ["idk\n"])

    def test_add_question_to_file(self):
        self.repo.load_certain_file("tests1.txt")
        self.repo.add_question_to_file(Question("1", "1", "1", "2", "3", "1", "easy"))
        self.assertEqual(self.repo.get_questions(), ['1;Which number is the largest;1;4;3;4;easy\n',
                                                     '2;Which number is the smallest;-3;3;0;-3;easy\n',
                                                     '3;Which number is prime;2;32;9;2;easy\n',
                                                     '4;Which country has the largest GDP;Brazil;China;UK;China;medium\n',
                                                     '5;Which is not a fish;carp;orca;eel;orca;medium\n',
                                                     '6;Name the first satellite;Apollo;Sputnik;Zaria;Sputnik;medium\n',
                                                     '7;Which Apollo mission did not make it to the moon;11;13;17;13;hard\n',
                                                     '8;A mole can be;animal;quantity;both;both;hard\n',
                                                     "9;Name El Cid's horse;Babieca;Abu;Santiago;Babieca;hard\n",
                                                     '10;The Western Roman Emprire fell in;654;546;476;476;hard\n',
                                                     '1;1;1;2;3;1;easy',
                                                     '1;1;1;2;3;1;easy'])

    def tearDown(self):
        self.repo = None


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.repo = Repository("test3.txt")
        self.service = Gameservice(self.repo, Validator())

    def test_check_if_good(self):
        self.assertEqual(self.service.check_if_good("4", "1;Which number is the largest;1;4;3;4;easy"), 1)
        self.assertEqual(self.service.check_if_good("4", "1;Which number is the largest;1;4;3;4;medium"), 2)
        self.assertEqual(self.service.check_if_good("4", "1;Which number is the largest;1;4;3;4;hard"), 3)
        self.assertEqual(self.service.check_if_good("1", "1;Which number is the largest;1;4;3;4;hard"), 0)

    def test_add_quiz(self):
        self.repo.create_file(['1;Which number is the largest;1;4;3;4;easy\n',
                               '2;Which number is the smallest;-3;3;0;-3;easy\n',
                               '3;Which number is prime;2;32;9;2;easy\n',
                               '4;Which country has the largest GDP;Brazil;China;UK;China;medium\n',
                               '5;Which is not a fish;carp;orca;eel;orca;medium\n',
                               '6;Name the first satellite;Apollo;Sputnik;Zaria;Sputnik;medium\n',
                               '7;Which Apollo mission did not make it to the moon;11;13;17;13;hard\n',
                               '8;A mole can be;animal;quantity;both;both;hard\n',
                               "9;Name El Cid's horse;Babieca;Abu;Santiago;Babieca;hard\n",
                               '10;The Western Roman Emprire fell in;654;546;476;476;hard\n'],
                              "test3.txt")
        self.repo.load_certain_file("test3.txt")
        self.service.add_quiz('1;Which number is the largest;1;4;3;4;easy')
        self.assertEqual(self.repo.get_questions(), ['1;Which number is the largest;1;4;3;4;easy\n',
                                                     '2;Which number is the smallest;-3;3;0;-3;easy\n',
                                                     '3;Which number is prime;2;32;9;2;easy\n',
                                                     '4;Which country has the largest GDP;Brazil;China;UK;China;medium\n',
                                                     '5;Which is not a fish;carp;orca;eel;orca;medium\n',
                                                     '6;Name the first satellite;Apollo;Sputnik;Zaria;Sputnik;medium\n',
                                                     '7;Which Apollo mission did not make it to the moon;11;13;17;13;hard\n',
                                                     '8;A mole can be;animal;quantity;both;both;hard\n',
                                                     "9;Name El Cid's horse;Babieca;Abu;Santiago;Babieca;hard\n",
                                                     '10;The Western Roman Emprire fell in;654;546;476;476;hard\n',
                                                     '1;Which number is the largest;1;4;3;4;easy'])

    def test_create_quiz(self):
        self.repo.load_file()
        self.service.create_quiz("easy 3 testcreate.txt")

    def tearDown(self):
        self.service = None
