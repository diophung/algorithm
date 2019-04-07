"""
Find the absolute difference between two diagonal lines in a N x N matrix
"""
import math


class Matrix:
    @staticmethod
    def get_abs_diff(matrix):
        """
        Find the absolute difference between 2 diagonal lines in a N x N matrix
        @:param matrix: N x N 2-d matrix
        :return: absolute difference between 2 sums, as integer
        """
        l = len(matrix)
        down_diagonal_sum = 0
        up_diagonal_sum = 0
        for i in range(l):
            down_diagonal_sum += matrix[i][i]
        for j in range(l):
            up_diagonal_sum += matrix[l - j - 1][j]
        return int(math.fabs(up_diagonal_sum - down_diagonal_sum))


m = [
    [12, 2, 1],
    [4, 5, 6],
    [1, 8, 9]
]
print(Matrix.get_abs_diff(m))
