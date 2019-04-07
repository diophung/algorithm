"""
LeetCode #273: Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


def int_to_word(num):
    """
    """
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
              'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
              'seventeen', 'eighteen', 'nineteen']
    
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = ['hundred']
    thousand = ['thousand']
    million = ['million']
    billion = ['billion']
    
    word = ""
    while num > 0:
        d = num / 10
        word += digits[d] + " "
        num = num / 10
    
    return word


print(int_to_word(1))  # one
print(int_to_word(11))  # eleven
print(int_to_word(12))  # twelve
print(int_to_word(89))  # eighty nine
print(int_to_word(123))  # one hundred twenty three
# print(int_to_word(1234))
# print(int_to_word(12345))
# print(int_to_word(123456))
# print(int_to_word(1234567))
# print(int_to_word(12345678))
# print(int_to_word(123456789))
