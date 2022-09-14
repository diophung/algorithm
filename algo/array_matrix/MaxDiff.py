# problem : maximum difference: find the max difference
# between any 2 numbers P, Q in an array_matrix, given P < Q
# and P appear before Q

# Algo 1: O(N^2)
# start with first date: buyPrice = prices[day0],
# profit = 0, sellPrice = buyPrice
#
# move on newDate:
#
# if found better buyPrice:
#     update buyPrice
# update profit as we move each day
#
import sys


class MaxDiff:
    @staticmethod
    def max_diff(prices_list):
        min_buy_price = int(sys.maxsize)
        profit = -1 * int(sys.maxsize)
        for index, item in enumerate(prices_list):
            # found better buy price
            if item < min_buy_price:
                min_buy_price = item
            # compare the profit generated today vs. the min so far
            profit = max(profit, item - min_buy_price)
        return profit


# expected 0
prices = [1, 1]

print(MaxDiff.max_diff(prices))

# expect 20 (25-5)
prices = [5, 12, 25, 1, -20]
print(MaxDiff.max_diff(prices))

# expect 3 (4-1)
prices = [1, 2, 3, 4]
print(MaxDiff.max_diff(prices))

# expect 0
prices = [4, 3, 2, 1]
print(MaxDiff.max_diff(prices))
