import unittest
import ordinal

class oridinalTest(unittest.TestCase):

    def isequal_1(self):
        self.assertEqual(ordinal(1), "1st")

    def isequal_2(self):
        self.assertEqual(ordinal(2), "2nd")

    def isequal_3(self):
        self.assertEqual(ordinal(3), "3rd")

    def isequal_3(self):
        self.assertEqual(ordinal(3), "3nd")

    def isequal_1233(self):
        self.assertEqual(ordinal(123), "123nd")

if __name__ == '__main__':
  unittest.main()
