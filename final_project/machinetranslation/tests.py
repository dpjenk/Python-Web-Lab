import unittest
from translator import english_to_french
from translator import french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertEqual(french_to_english("Bonjour"), "Hello")
unittest.main()   