# Problem : determine if a string can be constructured by taking a substring
# of it and appending multiple copies of that substring.
#
# Algorithm:
# Use a dictionary to store the count for each character
# Scan the dictionary, if there is a


class RepeatedSubstringPattern:
    @staticmethod
    def solution(s: str) -> bool:
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


print(RepeatedSubstringPattern.solution("abab"))  # ab * 2, expected True
print(RepeatedSubstringPattern.solution("ababc"))  # False
print(RepeatedSubstringPattern.solution("123123123"))  # 123 * 3, expected True
print(RepeatedSubstringPattern.solution("aa"))  # a * 2, True
print(RepeatedSubstringPattern.solution("aabb"))  # False
