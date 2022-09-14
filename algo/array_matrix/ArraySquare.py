import unittest


class FindSquareSoln:

    @staticmethod
    def find_square(arr1, arr2, y=None):
        """
        given 2 arrays a1, a2 containing integers,
        find items in a2 which is the square of items in a1
        """
        return [y for x in (arr1, y in arr2) if x * x == y]


