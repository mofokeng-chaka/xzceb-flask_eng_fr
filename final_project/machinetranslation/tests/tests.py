import unittest
from ibm_watson import ApiException
from translator import french_to_english, english_to_french


class TestTranslatorMethods(unittest.TestCase):
    def test_french_to_english_returns_correct_translation(self):
        expected_english_text = 'Hello'
        translated_english_text = french_to_english('Bonjour')
        self.assertEqual(expected_english_text, translated_english_text)

    def test_null_input_for_french_to_english(self):
        with self.assertRaises((NameError, ValueError)) :
            french_to_english(None)

    def test_non_existing_french_word_returns_the_same_word(self):
        non_existing_word = 'Xopsj'
        translated_english_text = french_to_english(non_existing_word)
        self.assertEqual(non_existing_word, translated_english_text)

    def test_english_to_french_returns_correct_translation(self):
        expected_french_text = 'Bonjour'
        translated_french_text = english_to_french('Hello')
        self.assertEqual(expected_french_text, translated_french_text)

    def test_null_input_for_englishToFrench(self):
        with self.assertRaises((NameError, ValueError)):
            english_to_french(None)

    def test_non_existing_english_word_returns_the_same_word(self):
        non_existing_word = 'Lzxci'
        translated_french_text = english_to_french(non_existing_word)
        self.assertEqual(non_existing_word, translated_french_text)

if __name__ == '__main__':
    unittest.main()
