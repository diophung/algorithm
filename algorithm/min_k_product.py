import sys
import unittest


def min_product(a, b, k):
    """
    Return k minimum products of two elements
    from 2 lists of sorted positive integers.
    ---
    O(k * min(A, B))
    """
    result = []
    len_a, len_b = len(a), len(b)
    min_idx_of_b = [0] * len_a
    if k > len_a * len_b:
        raise ValueError("Unable to get {} products".format(k))
    while k > 0:
        min_pr = sys.maxsize
        min_idx = 0
        for i in range(len_a):
            # take a element from A * min element from B
            p = a[i] * b[min_idx_of_b[i]]

            # found min prod and idx still valid
            if p < min_pr and min_idx_of_b[i] < len_b:
                min_pr = p
                min_idx = i

        # print('result={0: >20}, min_idx_of_b={1: >20}, min_idx={2: >20}'.format(result, min_idx_of_b, min_idx))
        result.append((a[min_idx], b[min_idx_of_b[min_idx]]))

        # increment min index which used in lst_b
        min_idx_of_b[min_idx] += 1
        k -= 1
    return result


class MinKProductTest(unittest.TestCase):

    def test_k_min_product(self):
        a = [10, 20, 40]
        b = [20, 30, 50, 90]
        k = 3
        expected = [(10, 20), (10, 30), (20, 20)]
        self.assertEquals(min_product(a, b, k), expected)

        a = [1]
        b = [1]
        k = 1
        expected = [(1, 1)]
        self.assertEquals(min_product(a, b, k), expected)

    def test_k_min_product_negative(self):
        a = [1]
        b = [1]
        k = 2
        with self.assertRaises(ValueError):
            min_product(a, b, k)


if __name__ == "__main__":
    unittest.main()
