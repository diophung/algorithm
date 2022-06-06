# Problem: determine if 2 strings are anagrams
# Solution 1 : O(nlogn) : compared sorted strings.
import unittest


def is_anagram_with_sorting(str_a, str_b):
    """
    check if 2 strings are anagrams
    @params str_a : the first string
    @params str_b : the second string
    """
    if str_a is None or str_b is None:
        return False
    sorted_a = sorted(str_a)
    sorted_b = sorted(str_b)
    return sorted_a == sorted_b


def dict_from_string(st):
    """
    convert a string into dictionary of characters
    """
    # assume Latin-charset
    d = [None] * 26
    for i in st:
        if d[ord(i) - 97] is None:  # ord('a') = 97
            d[ord(i) - 97] = 1
        else:
            d[ord(i) - 97] += 1
    return d


# Solution 2: compare count of characters, assume only Latin char (26-char)
def is_anagram_without_sorting(a, b):
    if a is None or b is None or len(a) != len(b):
        return False
    dict_a = dict_from_string(a)
    dict_b = dict_from_string(b)
    for i in range(len(dict_a)):
        if dict_a[i] != dict_b[i]:
            return False
    return True


class TestRun(unittest.TestCase):

    def test_sort_soln(self):
        self.assertTrue(is_anagram_with_sorting("tod", "dot"))
        self.assertFalse(is_anagram_with_sorting("bat", "bacteria"))
        self.assertFalse(is_anagram_with_sorting(None, "N"))

    def test_nonsort_soln(self):
        self.assertTrue(is_anagram_without_sorting("bat", "tab"))
        self.assertFalse(is_anagram_without_sorting("bac", "bacteria"))
        self.assertFalse(is_anagram_without_sorting(None, "N"))
