"""Module contains unit tests."""


import unittest

from utils import get_proper_name
from bot import check_if_username_is_in_list


class MyTestCase(unittest.TestCase):
    """Unit tests for the bot."""

    def test_func_get_proper_name_full_name(self):
        """Test case: full name, sent by a participant via message, is interpreted correctly."""
        formatted_name = get_proper_name("александра алексеева")
        self.assertEqual(formatted_name, "александра алексеева")

    def test_func_get_proper_name_surname_first(self):
        """Test case: surname with following name, sent by a participant via message, is interpreted correctly."""
        formatted_name = get_proper_name("кислов гена")
        self.assertEqual(formatted_name, "геннадий кислов")

    def test_func_get_proper_name_diminutive_name(self):
        """Test case: diminutive name, sent by a participant via message, is interpreted correctly."""
        formatted_name = get_proper_name("антошка терентьев")
        self.assertEqual(formatted_name, "антон терентьев")

    def test_get_proper_name_excess_words(self):
        """Test case: name with extra irrelevant words, sent by a participant via message, is interpreted correctly."""
        formatted_name = get_proper_name("ксюшка пушка гливко")
        self.assertEqual(formatted_name, "ксения гливко")

    def test_func_get_proper_name_not_in_list(self):
        """Test case: name of a person not in the list of participants is interpreted correctly."""
        formatted_name = get_proper_name("алиенора аквитанская")
        self.assertEqual(formatted_name, None)


if __name__ == "__main__":
    unittest.main()
