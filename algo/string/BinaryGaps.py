import unittest

class BinaryGaps:
    """
    A binary gap within a positive integer N is any maximal sequence of
    consecutive zeros that is surrounded by ones at both ends in the binary
    representation of N. For example, number 9 has binary representation 1001
    and contains a binary gap of length 2. The number 529 has binary
    representation 1000010001 and contains two binary gaps: one of length 4
    and one of length 3. The number 20 has binary representation 10100 and
    contains one binary gap of length 1. The number 15 has binary
    representation 1111 and has no binary gaps.
    Write a function:

        def solution(N)

    that, given a positive integer N, returns the length of its longest
    binary gap. The function should return 0 if N doesn't contain a binary gap.
    For example, given N = 1041 the function should return 5, because N has
    binary representation 10000010001 and so its longest binary gap is of length 5.

    Assume that: N is an integer within the range [1..2,147,483,647].

    Complexity:
    expected worst-case time complexity is O(log(N)).
    expected worst-case space complexity is O(1).
    """

    @staticmethod
    def count_gap(n):
        if n < 0:
            return -1
        if n <= 1:
            return 0
        binary_format_string = bin(n)[2:]
        max_val = 0
        has_started = False
        temp_counter = 0
        for digit in binary_format_string:
            if digit == "1":
                # starting seq
                if not has_started:
                    has_started = True
                    temp_counter = 0
                # ending seq
                if has_started:
                    if temp_counter > max_val:
                        max_val = temp_counter
                    temp_counter = 0
            if digit == "0":
                if has_started:
                    temp_counter += 1

        return max_val


class BinaryGapsCount(unittest.TestCase):

    def test_bin_gaps_count(self):
        bin_gap = BinaryGaps()
        self.assertEqual(bin_gap.count_gap(1041), 5)  # expect 5
        self.assertEqual(bin_gap.count_gap(0), 0)  # expect 0
        self.assertEqual(bin_gap.count_gap(1), 0)  # expect 0
        self.assertEqual(bin_gap.count_gap(10), 1)  # expect 1
