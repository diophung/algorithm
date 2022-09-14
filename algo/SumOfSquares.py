# Shortest sum of squares:
#   Based on LaGrange's theorem : any positive integer can be represented
#   with at most sum of 4 squares. Find the least number of sum of squares
#   which sums up to a integer number N
# For e.g:
# 13 = 3^2 + 2^2 -> sum_of_squares(13)= 2
# 16 = 4^2 -> sum_of_squares(16) = 1
import unittest

import math


def sum_of_squares(N):
    # Ago: let intSq = int(sqrt(N))
    # remains = N - intSq*intSq
    # if remains = 0:
    #    N is perfect_square -> return 1
    # if remains is perfect_square:
    #    N is sum of 2 perfect_square -> return 2
    # Return min(1 + sum_of_squares(remains), 4)

    square = int(math.sqrt(N))
    remains = N - square * square
    if remains == 0:
        return 1
    if math.sqrt(remains) == 0:
        return 2
    return min(4, 1 + sum_of_squares(remains))  # maximum = sum of 4 squares


class TestSumOfSquare(unittest.TestCase):

    def test_positive_case(self):
        self.assertEqual(sum_of_squares(10), 2)


print(sum_of_squares(10))  # 10 = 3^2 + 1^2 -> expect 2
print(sum_of_squares(13))  # 13 = 3^2 + 2^2 -> expect 2
print(sum_of_squares(15))  # 15 = 3^2 + 2^2 + 1^2 + 1^2 -> expect 4
print(sum_of_squares(16))  # 16 = 4^2 -> expect 1
print(sum_of_squares(1))  # expect 1 :
print(sum_of_squares(17))  # expect 2 : 4^2 + 1^2

if __name__ == "__main__":
    print(sum_of_squares(10))
