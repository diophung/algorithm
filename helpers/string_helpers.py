import unittest

def char_to_int(string):
    return ord(string) - 97


def int_to_char(number):
    return chr(number)


class Solution:

    def test(self):
        v = char_to_int("a")
        print(v)


class SlnTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(char_to_int("a"), 0)


if __name__ == "__main__":
    unittest.main()
