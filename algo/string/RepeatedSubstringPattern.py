# Problem : determine if a string can be constructed by taking a substring
# of it and appending multiple copies of that substring.
#
# Algorithm:
# Use a dictionary to store the count for each character
# Scan the dictionary, if there is a


class RepeatedSubstringPattern:
    @staticmethod
    def can_build(s: str) -> bool:
        substr = ''
        max_size = int(len(s) / 2) + 1  # multiply multiple times, must be > 1
        for i in range(max_size):
            substr += s[i]
            # possible repetition
            if len(s) % len(substr) == 0:
                multiplier = int(len(s) / len(substr))
                if substr * multiplier == s:
                    return True
        return False


print(RepeatedSubstringPattern.can_build("abab"))  # ab * 2, expected True
print(RepeatedSubstringPattern.can_build("ababc"))  # False
print(RepeatedSubstringPattern.can_build("123123123"))  # 123 * 3, expected True
print(RepeatedSubstringPattern.can_build("aa"))  # a * 2, True
print(RepeatedSubstringPattern.can_build("aabb"))  # False
