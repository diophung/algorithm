"""
LeetCode #273: Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
MAX       = 1000000000000
BILLION   = 1000000000
MILLION   = 1000000
THOUSAND  = 1000
HUNDRED   = 100
TWENTY    = 20

digits = [   'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
              'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen','seventeen', 'eighteen', 'nineteen']
    
tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']


def to_thousand(num):
    word = ""

    if HUNDRED <= num < THOUSAND:
        d = int(num / HUNDRED)
        num = num % HUNDRED
        word += digits[d] + ' hundred '
        if num == 0:
            return word

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
    word = ""
    if num > MAX:
        raise ValueError("number too big. Max is {}".format(MAX))
    if num >= BILLION:
        d = num / BILLION
        num = num % BILLION
        word += to_thousand(d) + ' billion '
        if num == 0:
            return word
        
    if num >= MILLION:
        d = num / MILLION
        num = num % MILLION
        word += to_thousand(d) + ' million '
        if num == 0:
            return word
        
    if num >= THOUSAND:
        d = num / THOUSAND
        num = num % THOUSAND
        word += to_thousand(d) + ' thousand '
        if num == 0:
            return word
        
    if num >= HUNDRED:
        d = num / HUNDRED
        num = num % HUNDRED
        word += to_thousand(d) + ' hundred '
        if num == 0:
            return word
        
    if num >= TWENTY:
        d = int(num / 10)
        num = num % 10
        word += tens[d]
        
    if 0 <= num < TWENTY:
        d = num % 20
        word += digits[d]
        
    return word


print(int_to_word(100))  # one hundred
print(int_to_word(1000))  # one thousand
print(int_to_word(1000000))  # one million
print(int_to_word(1000000000))  # one billion
print(int_to_word(0))  # zero
print(int_to_word(1))  # one
print(int_to_word(5))  # one
print(int_to_word(11))  # eleven
print(int_to_word(12))  # twelve
print(int_to_word(20))  # twenty
print(int_to_word(21))  # twenty one
print(int_to_word(35))  # thirty five
print(int_to_word(89))  # eighty nine
print(int_to_word(123))  # one hundred twenty three
print(int_to_word(1234)) # 1,234: one thousand two hundred thirty four
print(int_to_word(12345)) # 12,345: twelve thousand three hundred fourty five
print(int_to_word(123456)) # 123,456: one hundred twenty three thousand four hundred fifty six
print(int_to_word(1234567))  # 1,234,567: one million two hundre thirty four thousand 
print(int_to_word(12345678)) # 12,345,678: twelve million three hundred fourty five thousand six hundred seventy eight
print(int_to_word(123456789)) # 123,456,789: one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
print(int_to_word(123123456789)) 
print(int_to_word(100000)) 
print(int_to_word(100000000)) 
print(int_to_word(100000000000)) 
print(int_to_word(100000000001)) 
