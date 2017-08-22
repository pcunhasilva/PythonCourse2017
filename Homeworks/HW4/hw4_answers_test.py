import unittest
import random
import hw4_answers

class SortTest(unittest.TestCase):

    def setUp(self):
        self.test1 = [1, 2, 2, 40, 0, 3, 5, 5]
        self.sortedtest1 = sorted(self.test1)
        self.test2 = [-1, -5, -10, -2, 0, 3, 2, 3, 3, 3]
        self.sortedtest2 = sorted(self.test2)

    # Test selection:
    def test_positive_selection(self):
        self.assertEqual(hw4_answers.selection(self.test1), self.sortedtest1)
    def test_positive_negative_selection(self):
        self.assertEqual(hw4_answers.selection(self.test2), self.sortedtest2)

    # Test counting:
    def test_positive_counting(self):
        self.assertEqual(hw4_answers.counting(self.test1), self.sortedtest1)
    def test_positive_negative_counting(self):
        self.assertEqual(hw4_answers.counting(self.test2), self.sortedtest2)

    # Test counting equal selection
    def test_positive_selection_counting(self):
        self.assertEqual(hw4_answers.counting(self.test1), hw4_answers.selection(self.test1))
    def test_positive_negative_selection_counting(self):
        self.assertEqual(hw4_answers.counting(self.test2), hw4_answers.selection(self.test2))

if __name__ == '__main__':
  unittest.main()
