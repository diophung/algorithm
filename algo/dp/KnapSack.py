import unittest


def knapsack(pairs, W):
    """
    Given list of pairs with format (weight, value) and a knapsack that can carry MAX_WEIGHT
    Get the maximum total value in the knapsack.
    Args:
        pairs (list[pair]): input as [(weight1, value1), (weight2, value2)...]
        W (int): max capacity

    Returns:
        max value that can be achieved

    """

    wts = [pair[0] for pair in pairs]
    vals = [pair[1] for pair in pairs]
    LE = len(pairs)
    # map of value to weight, optimized at each cell
    dp = [[0 for x in range(W + 1)] for x in range(LE + 1)]

    for i in range(LE + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0

            # if more weight to consider
            # the need to maximize value
            # by comparing prev and current items
            elif wts[i - 1] <= w:
                remaining_weight = W - wts[i - 1]
                new_val = vals[i - 1] + dp[i - 1][remaining_weight]
                other_val = dp[i - 1][w]

                # choose the better one
                dp[i][w] = max(new_val, other_val)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[LE][W]


def knapsack_recur(weights, values, max_weight, n):
    if n == 0 or max_weight == 0:
        return 0

    # if this item should not be in the knapsack
    if weights[n - 1] > max_weight:
        return knapsack_recur(weights, values, max_weight, n - 1)

    # else if this item might be in the optimized soln
    # then we choose the better out of
    # 1) include n-th item vs. 2) not include n-th item
    else:
        included = values[n - 1] + knapsack_recur(weights, values, max_weight - weights[n - 1], n - 1)
        not_included = knapsack_recur(weights, values, max_weight, n - 1)
        return max(included, not_included)


class KnapSackTest(unittest.TestCase):

    def test_knap_sack_positive(self):
        weight_value_pairs = [(3, 50), (1, 10), (1, 20), (1, 30)]  # W= 3, expect values = 10 + 20 + 30 
        weights = [pair[0] for pair in weight_value_pairs]
        values = [pair[1] for pair in weight_value_pairs]
        N = len(weights)
        W = 3
        val_dp = knapsack(weight_value_pairs, W)
        val_recur = knapsack_recur(weights, values, W, N)
        self.assertTrue(val_dp == 60)
        self.assertTrue(val_recur == 60)
