import unittest

from anagram import Anagram as anagram


class AnagramTest(unittest.TestCase):
    def test_empty_string_return_empty(self):
        expected = []
        self.assertEqual(expected, anagram.returnAnagram(""))

    def test_letter_should_return_itself(self):
        result_one = anagram.returnAnagram("a")
        result_two = anagram.returnAnagram("B")

        self.assertEqual(["a"], result_one)
        self.assertEqual(["B"], result_two)

        self.assertEqual(len(result_one), 1)
        self.assertEqual(len(result_two), 1)

    def test_word_with_length_two_should_return_max_result_2(self):
        result_one = anagram.returnAnagram("de")
        result_two = anagram.returnAnagram("fk")

        expected_one = ['de', 'ed']
        expected_two = ['fk', 'kf']

        self.assertCountEqual(result_one, expected_one)
        self.assertCountEqual(result_two, expected_two)

    def test_word_with_three_should_return_max_result_6(self):
        result_one = anagram.returnAnagram("cat")
        result_two = anagram.returnAnagram("dry")

        expected_one = ['cat', 'cta', 'act', 'atc', 'tac', 'tca']
        expected_two = ['dry', 'dyr', 'ryd', 'rdy', 'yrd', 'ydr']

        self.assertCountEqual(result_one, expected_one)
        self.assertCountEqual(result_two, expected_two)

    def test_word_with_repeated_letter_should_not_return_duplicate_result(self):
        result_one = anagram.returnAnagram("dd")
        result_two = anagram.returnAnagram("ebb")

        expected_one = ['dd']
        expected_two = ['ebb', 'beb', 'bbe']

        self.assertCountEqual(result_one, expected_one)
        self.assertCountEqual(result_two, expected_two)


if __name__ == '__main__':
    unittest.main()
