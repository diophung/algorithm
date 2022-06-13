import unittest


class KnapSack(object):
    def __init__(self):
        pass

    def solve_recur(self, weights, values, max_w, n):
        """
        given 2 arrays of weights and values, find the items that return the  most value within max weight
        Args:
            weights: array of weight
            values: array of value
            max_w: max possible weight
            n: size of the elements

        Returns:
            max possible value given max_weight
        """

        # base case
        if max_w == 0 or n == 0:
            return 0

        # if this item weight greater than W then
        # cannot include this in the optimal solution
        if weights[n - 1] > max_w:
            return self.solve_recur(weights, values, max_w, n - 1)

        # if to include this item, return the max between
        # - includes this item
        # - not include this item
        else:
            return max(
                values[n - 1] + self.solve_recur(weights, values, max_w - weights[n - 1], n - 1),  # include
                self.solve_recur(weights, values, max_w, n - 1)  # not include
            )


class KnapSackTest(unittest.TestCase):

    def test_knapsack_recursive(self):
        ks = KnapSack()
        weights = [2,  2,  2]
        values = [3, 4, 8]
        self.assertTrue(ks.solve_recur(weights, values, max_w=4, n=3), 12)

    def test_knapsack_recursive2(self):
        ks = KnapSack()
        weights = [1, 4]
        values = [3, 10]
        self.assertTrue(ks.solve_recur(weights, values, max_w=2, n=2), 0)
