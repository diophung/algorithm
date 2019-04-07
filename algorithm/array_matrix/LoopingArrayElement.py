import math
import unittest


def get_final_state(states, days):
    """
    states: array of 8 numbers with value of 1 or 0 | 1 = active, 0 = inactive
    days: integer.
    
    If left and right neighbors are both active or inactive -> the element is inactive next day.
    Otherwise, it's active the next day.For the two elements at both ends: assuming one of its
    neighbor is always inactive.
    
    Find the final value of "states" after "days".
    """
    current = [0] + states + [0]
    while days > 0:
        for i in range(1, len(current) - 1):
            states[i - 1] = int(math.fabs(current[i - 1] - current[i + 1]))
        current = [0] + states + [0]
        days -= 1
    
    return current[1:-1]


def generalize_gcd(num, arr):
    """
    Find the greatest common divider (GCD) of all elements in arr.
    
    num: int, the length of arr
    arr: array of ints
    """
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    res = arr[0]
    for i in range(1, num):
        res = gcd(res, arr[i])
    return res


class TestAmznSamples(unittest.TestCase):
    
    def test_cell_compete(self):
        cells = [1, 0, 1, 1, 1, 1, 0, 1]
        expected = [0, 0, 1, 0, 0, 1, 0, 0]
        actual = get_final_state(cells, 1)
        self.assertEquals(expected, actual)
    
    def test_generalize_gcd(self):
        arr = [2, 4, 6, 8, 10]
        exp = 2
        self.assertEquals(generalize_gcd(5, arr), exp)
        
        arr = [16, 8, 24]
        exp = 8
        self.assertEquals(generalize_gcd(3, arr), exp)


if __name__ == "__main__":
    unittest.main()
