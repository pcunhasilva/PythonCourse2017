import unittest
from ordinal import myfunction

class ordinal_Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_equal_to_1(self):
        self.assertEqual(myfunction(1), "1st")

    def test_is_equal_to_2(self):
        self.assertEqual(myfunction(2), "2nd")

    def test_is_equal_to_3(self):
        self.assertEqual(myfunction(3), "3rd")

    def test_is_equal_to_4(self):
        self.assertEqual(myfunction(4), "4th")

    def test_is_equal_to_123(self):
        self.assertEqual(myfunction(123), "123rd")

    def test_not_equal_to_123(self):
        self.assertNotEqual(myfunction(123), "123st")

if __name__ == '__main__':
    unittest.main()
