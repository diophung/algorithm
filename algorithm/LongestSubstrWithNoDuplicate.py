# Problem: given a string s, find the longest substring without duplicated character
# For e.g:
# abcabcbb --> "abc"
# bbbb -> "b"
# pwwkew -> "wke", note that "pkew" is a subsequence, not a substring.


# Algorithm:
# Use a dictionary to store where each character appears in the string.
# If we found a repeated character:
#   Assume the new substring start there
#
# Update the index of each character
# Update max length: compare current max len with length of new substring
class LongestSubstring:
    @staticmethod
    def get_longest_unique_substring(s):
        chars = {}
        length = len(s)
        start = -1
        max_len = 0
        for index in range(length):
            if s[index] in chars:
                # repeated char, assume it's the start of the longest substr
                start = max(start, chars[s[index]])
            chars[s[index]] = index
            max_len = max(max_len, index - start)
        return max_len


print("expect : 3 = " + str(LongestSubstring.get_longest_unique_substring("abcabcbb")))  # abc -> 3
print("expect : 1 = " + str(LongestSubstring.get_longest_unique_substring("bbbb")))  # b -> 1
print("expect : 3 = " + str(LongestSubstring.get_longest_unique_substring("pwwkew")))  # wke -> 3
print("expect : 4 = " + str(LongestSubstring.get_longest_unique_substring("abcabcd")))  # abcd -> 4
print("expect : 5 = " + str(LongestSubstring.get_longest_unique_substring("abcdaabcdec")))  # abcde -> 5
print("expect : 0 = " + str(LongestSubstring.get_longest_unique_substring("")))  # None -> 0
print("expect : 1 = " + str(LongestSubstring.get_longest_unique_substring(" ")))  # Space -> 1
print("expect : 1 = " + str(LongestSubstring.get_longest_unique_substring("a")))  # a -> 1
print("expect : 4 = " + str(LongestSubstring.get_longest_unique_substring("abccabd")))  # cbda -> 4
