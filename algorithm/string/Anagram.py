# Problem: determine if 2 strings are anagrams
# Solution 1 : O(nlogn) : compared sorted strings.


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


print(is_anagram_with_sorting("tod", "dot"))  # expect True
print(is_anagram_with_sorting("bat", "bacteria"))  # expect False
print(is_anagram_with_sorting(None, "N"))  # expect False


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


print(is_anagram_without_sorting("bat", "tab"))  # expect True
print(is_anagram_without_sorting("bac", "bacteria"))  # expect False
print(is_anagram_without_sorting(None, "N"))  # expect False
