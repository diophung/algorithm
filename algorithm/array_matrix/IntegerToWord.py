"""
LeetCode #273: Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than X (TBD).

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
import math

MAX = int(math.pow(2, 31) - 1)
BILLION = 1000000000
MILLION = 1000000
THOUSAND = 1000
HUNDRED = 100
TWENTY = 20

digits = ['zero', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ',
          'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ',
          'eighteen ', 'nineteen ']
    
tens = ['zero', 'ten ', 'twenty ', 'thirty ', 'forty ',
        'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ', 'hundred ']


def __int_to_word_by_range(word, num, base, string):
    if num >= base:
        d = int(num / base)
        num = num % base
        word += __base_prefix(d) + string
        if num == 0:
            return word, num
    return word, num


def __base_prefix(num):
    word = ""
    word, num = __int_to_word_by_range(word, num, HUNDRED, 'hundred ')
    if 20 <= num < HUNDRED:
        d = int(num / 10)
        num = num % 10
        word += tens[d]
        if num == 0:
            return word
    
    if 0 < num < 20:
        d = int(num % 20)
        word += digits[d]

    return word


def int_to_word(num):
    orig = num
    word = ""
    if num > MAX:
        raise ValueError("number too big. Max is {}".format(MAX))
    
    if num == 0:
        return 'zero'
    word, num = __int_to_word_by_range(word, num, BILLION, 'billion ')
    word, num = __int_to_word_by_range(word, num, MILLION, 'million ')
    word, num = __int_to_word_by_range(word, num, THOUSAND, 'thousand ')
    word, num = __int_to_word_by_range(word, num, HUNDRED, 'hundred ')

    # handling special case: "eleven", "twelve" etc
    if num >= TWENTY:
        d = int(num / 10)
        num = num % 10
        word += tens[d]
        
    if 0 < num < TWENTY:
        d = int(num % 20)
        word += digits[d]
    print("{:,}".format(orig))
    return word + '\n'


print(int_to_word(1))
print(int_to_word(10))
print(int_to_word(100))  # one hundred
print(int_to_word(1000))  # one thousand
print(int_to_word(10000))
print(int_to_word(10001))
print(int_to_word(11000))
print(int_to_word(1000000))  # one million
print(int_to_word(100000000)) 
print(int_to_word(1000000000))  # one billion
print(int_to_word(0))  # zero
print(int_to_word(1))  # one
print(int_to_word(5))  # one
print(int_to_word(10))  # ten
print(int_to_word(11))  # eleven
print(int_to_word(12))  # twelve
print(int_to_word(20))  # twenty
print(int_to_word(21))  # twenty one
print(int_to_word(35))  # thirty five
print(int_to_word(89))  # eighty nine
print(int_to_word(123))  # one hundred twenty three
print(int_to_word(1234))  # 1,234: one thousand two hundred thirty four
print(int_to_word(12345))  # 12,345: twelve thousand three hundred forty five
print(int_to_word(123456))  # 123,456: one hundred twenty three thousand four hundred fifty six
print(int_to_word(1234567))  # 1,234,567: one million two hundred thirty four thousand
print(int_to_word(12345678))  # 12,345,678: twelve million three hundred forty five thousand six hundred seventy eight
print(int_to_word(123456789))  # 123,456,789: one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
print(int_to_word(math.pow(2, 31) - 2)) 
