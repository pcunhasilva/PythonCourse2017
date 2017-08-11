import unittest
import lab3

class lab3Code(unittest.TestCase):

    def setUp(self):
        self.txt_string_long = "Say hi."
        self.txt_string = "Say"
        self.txt_number = 234

    # Test shout:

    def test_shout_string_long(self):
        self.assertEqual(lab3.shout(self.txt_string_long), "SAY HI!")

    def test_shout_string(self):
        self.assertEqual(lab3.shout(self.txt_string), "SAY!")

    def test_shout_string2(self):
        self.assertEqual(lab3.shout("blah"), "BLAH!")

    def test_shout_number(self):
        self.assertEqual(lab3.shout(self.txt_number), "234!")

    # Test reverse:

    def test_reverse_string(self):
        self.assertEqual(lab3.reverse(self.txt_string), "yaS")

    def test_reverse_number(self):
        self.assertEqual(lab3.reverse(self.txt_number), "432")

    # Test reversewords:

    def test_reversewords_string(self):
        self.assertEqual(lab3.reversewords(self.txt_string_long), "hi. Say")

    def test_reversewords_number(self):
        self.assertEqual(lab3.reversewords(self.txt_number), "234")

    def test_reversewords_error(self):
        self.assertRaises(lab3.reversewords(self.txt_string))

    # Test reversewordletters:

    def test_reversewordletters_string(self):
        self.assertEqual(lab3.reversewordletters(self.txt_string_long), ".ih yaS")

    def test_reversewordletters_error1(self):
        self.assertRaises(lab3.reversewordletters(self.txt_number))

    def test_reversewords_error2(self):
        self.assertRaises(lab3.reversewordletters(self.txt_string))

#reversewordletters

if __name__ == '__main__':
  unittest.main()
