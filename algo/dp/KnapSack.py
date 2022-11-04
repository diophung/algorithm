import unittest


def knapsack_dp(pairs, MAX_W):
    """
    Given list of pairs with format (weight, value) and a knapsack that can carry MAX_WEIGHT
    Get the maximum total value in the knapsack.
    Args:
        pairs (list[pair]): input as [(weight1, value1), (weight2, value2)...]
        MAX_W (int): max capacity

    Returns:
        max value that can be achieved

    """

    weights = [pair[0] for pair in pairs]
    values = [pair[1] for pair in pairs]
    n = len(pairs)
    # map of value to weight, optimized at each cell
    dp = [[0 for x in range(MAX_W + 1)] for x in range(n + 1)]

    for i in range(n):
        for w in range(MAX_W + 1):
            # choose the best between including or excluding this item
            if weights[i] <= w:
                included = values[i] + dp[i][w - weights[i]]
                excluded = dp[i][w]
                dp[i + 1][w] = max(included, excluded)
            else:
                # this item can't be included
                dp[i + 1][w] = dp[i][w]

    return dp[n][MAX_W]


def knapsack_recur(weights, values, MAX_W, n):
    """
    Given list of weights and values and a MAX_W (weight)
    Find the optimal value to put in the knapsack
    Args:
        weights (list[int]):
        values (list[int]):
        MAX_W (int): max weight allowed
        n (int): size of arrays

    Returns:
        best value possible

    """
    if n == 0 or MAX_W == 0:
        return 0

    # if this item should not be in the knapsack
    if weights[n - 1] > MAX_W:
        return knapsack_recur(weights, values, MAX_W, n - 1)

    # else if this item might be in the optimized soln
    # then we choose the better out of
    # 1) include n-th item vs. 2) not include n-th item
    else:
        included = values[n - 1] + knapsack_recur(weights, values, MAX_W - weights[n - 1], n - 1)
        not_included = knapsack_recur(weights, values, MAX_W, n - 1)
        return max(included, not_included)


class KnapSackTest(unittest.TestCase):
    # pairs of weight-value
    ITEMS = [(3, 50), (1, 10), (1, 20), (1, 30)]

    def test_knap_sack_recursive(self):
        weights = [p[0] for p in self.ITEMS]
        values = [p[1] for p in self.ITEMS]
        recur = knapsack_recur(weights, values, MAX_W=4, n=len(weights))
        self.assertEquals(80, recur)

    def test_knap_sack_dp(self):
        dp = knapsack_dp(self.ITEMS, MAX_W=4)
        self.assertEqual(80, dp)
