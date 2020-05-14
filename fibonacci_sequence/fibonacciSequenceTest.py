import unittest

from fibonacci_sequence import fibonacciSequence


class FibonacciTest(unittest.TestCase):

    def test_should_return_zero_for_position_zero(self):
        result: [] = fibonacciSequence.getListOfSequentialValues(1)
        self.assertEqual([0], result)

    def test_should_return_two_numbers_from_list(self):
        result: [] = fibonacciSequence.getListOfSequentialValues(2)
        self.assertEqual([0, 1], result)

    def test_should_return_three_numbers_from_list(self):
        result: [] = fibonacciSequence.getListOfSequentialValues(3)
        self.assertEqual([0, 1, 1], result)

    def test_should_return_21_for_fibonacci_8(self):
        result: [] = fibonacciSequence.getListOfSequentialValues(8)
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13], result)

    def test_should_return_ordered_150_numbers_of_fibonnaci(self):
        result: [] = fibonacciSequence.getListOfSequentialValues(150)
        self.assertEqual(150, len(result))


if __name__ == '__main__':
    unittest.main()
