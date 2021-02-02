import unittest

from utils import participants_surnames, get_proper_name
from bots import participants, check_if_in_list


class MyTestCase(unittest.TestCase):

    def test_func_get_proper_name_surname_first(self):
        formatted_name = get_proper_name("кислов гена")
        self.assertEqual(formatted_name, "геннадий кислов")

    def test_func_get_proper_name_diminutive_name(self):
        formatted_name = get_proper_name("антошка терентьев")
        self.assertEqual(formatted_name, "антон терентьев")

    def test_get_proper_name_excess_words(self):
        formatted_name = get_proper_name("ксюшка пушка гливко")
        self.assertEqual(formatted_name, "ксения гливко")

    def test_func_get_proper_name_not_in_list(self):
        formatted_name = get_proper_name("алиенора аквитанская")
        self.assertEqual(formatted_name, None)

    def test_func_check_if_in_list_not_participant(self):
        formatted_name = check_if_in_list("алиенора аквитанская")
        self.assertEqual(formatted_name, "Ошибочка вышла, перепроверь своё имя, умник... Или умница... Вы имеете право сами определять свой гендер.")



if __name__ == '__main__':
    unittest.main()
