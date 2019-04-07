# Shortest sum of squares:
#   Based on LaGrange's theorem : any positive integer can be represented
#   with at most sum of 4 squares. Find the least number of sum of squares
#   which sums up to a integer number N
# For e.g:
# 13 = 3^2 + 2^2 -> sum_of_squares(13)= 2
# 16 = 4^2 -> sum_of_squares(16) = 1
import math


def sum_of_squares(N):
    # Ago: let intSq = int(sqrt(N))
    # remains_N = N - intSq*intSq
    # if remains_N = 0:
    #    N is perfect_square -> return 1
    # if remains_N is perfect_square:
    #    N is sum of 2 perfect_square -> return 2
    # Return min(1 + sum_of_squares(remains_N), 4)

    int_sqrt = int(math.sqrt(N))
    remains_N = N - int_sqrt * int_sqrt
    if remains_N == 0:
        return 1
    if math.sqrt(remains_N) == 0:
        return 2
    return min(4, 1 + sum_of_squares(remains_N))  # maximum = sum of 4 squares


print(sum_of_squares(10))  # 10 = 3^2 + 1^2 -> expect 2
print(sum_of_squares(13))  # 13 = 3^2 + 2^2 -> expect 2
print(sum_of_squares(15))  # 15 = 3^2 + 2^2 + 1^2 + 1^2 -> expect 4
print(sum_of_squares(16))  # 16 = 4^2 -> expect 1
print(sum_of_squares(1))   # expect 1 :
print(sum_of_squares(17))  # expect 2 : 4^2 + 1^2
