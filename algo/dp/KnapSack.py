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

    def solve_dp(self, weights, values, max_w, n):
        dp = [[0 for x in range(max_w + 1)] for y in range(n + 1)]

        # build table KS[value][weight]
        for i in range(n + 1):
            for w in range(max_w + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif weights[i - 1] < max_w:  # this item can be in the optimal solution
                        dp[i][w] = max(
                            values[i - 1] + dp[i - 1][w - weights[i-1]],  # include this item
                            dp[i - 1][w]                                 # not include this item
                        )
                else:
                    dp[i][w] = dp[i-1][w]  # this item cannot be in optimal solution
        return dp[n][max_w]


class KnapSackTest(unittest.TestCase):

    def test_knapsack(self):
        ks = KnapSack()
        weights = [2,  2,  2]
        values = [3, 4, 8]
        self.assertTrue(ks.solve_recur(weights, values, max_w=4, n=3), 12)
        self.assertTrue(ks.solve_dp(weights, values, max_w=4, n=3), 12)

    def test_knapsack2(self):
        ks = KnapSack()
        weights = [2,  4]
        values = [5, 10]
        self.assertTrue(ks.solve_recur(weights, values, max_w=3, n=2), 5)
        self.assertTrue(ks.solve_dp(weights, values, max_w=3, n=2), 5)

    def test_knapsack_negative(self):
        ks = KnapSack()
        weights = [1, 4]
        values = [3, 10]
        self.assertTrue(ks.solve_recur(weights, values, max_w=2, n=2), 0)
        self.assertTrue(ks.solve_dp(weights, values, max_w=2, n=2), 0)
