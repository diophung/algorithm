# problem: given a signed 64-bit integer N, form the largest possible number
# with just the digits of N (and with the negative sign)
# i.e :  solution(144624) = 644421
#       solution(-321) = -123
import sys


class Solution:
    @staticmethod
    def max_int_given_digits(input_number):
        num = int(input_number)
        digits = list(str(num))
        # asc order, only work with negative int.
        digits.sort()
        if num > 0:
            digits.reverse()
        str_max = "".join(digits)
        return int(str_max)


print("""Given N as a 64-bit signed integer,
create the largest int using just the digits in N.""")

s = Solution()
print('Max possible int: ' + str(s.max_int_given_digits(144624)))  # 644421
print('Max possible int: ' + str(s.max_int_given_digits(-321)))  # -123
print('Max possible int: ' + str(s.max_int_given_digits(0)))  # 0
print(sys.maxint)
print('Max possible int: ' + str(s.max_int_given_digits(sys.maxint)))
