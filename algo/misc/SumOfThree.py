import math
import random
import unittest


class SumOfTwo:
    @staticmethod
    def find_pairs(sorted_array, target):
        """
        Return all unique paris that sum up to "target"
        Args:
            sorted_array (list[int]): input array
            target (int): target number

        Returns:
            list of unique pair (x,y)
        """

        """
        algo:
            sort the list
            keep two indexes: start, end
            curr = ints[start] + int[end]
            while start != end:
                if curr == target -> check uniqueness, add to output, increase start & reduce end
                if curr > target --> reduce end
                if curr < target --> increase start
        """
        if len(sorted_array) < 2:
            return []
        result = []
        sorted_array = sorted(sorted_array)
        start = 0
        end = len(sorted_array) - 1
        while start < end:
            curr = sorted_array[start] + sorted_array[end]
            if curr == target:
                if (sorted_array[start], sorted_array[end]) not in result:
                    result.append((sorted_array[start], sorted_array[end]))
                start += 1
                end -= 1
            elif curr > target:
                end -= 1
            elif curr < target:
                start += 1
        return result


class SumOfThree:
    @staticmethod
    def find_triplets(ints, target):
        """
        Return all unique triplets those sum up to "target"
        Args:
            ints (list[int])): array of integers
            target (int): target number

        Returns:
            list of unique triplets that sum up to target list[(a,b,c)]
        """

        """
        find_triplets algo:
            sort array by incr 
            for each (key ,value) in enumerate(array):
                pairs = find_pairs (remaining elements in array, new target = target - value)
                for each pair:
                    if (element, pairs[0], pairs[1]) is unique:
                        add to output
                    
        Algo for SumOfTwo:
            
        """
        output = []
        length = len(ints)
        ints = sorted(ints)
        for k, v in enumerate(ints):
            pairs = SumOfTwo.find_pairs(ints[k + 1: length], target - v)
            if pairs:
                for pair in pairs:
                    temp = sorted([v, pair[0], pair[1]])
                    if (temp[0], temp[1], temp[2]) not in output:
                        output.append((v, pair[0], pair[1]))
        return output


class SumOfNTests(unittest.TestCase):
    def test_find_sum_of_two(self):
        ints = [3, 0, -1, 2, 1, 2, 0]
        res = SumOfTwo.find_pairs(ints, 2)
        self.assertEqual([(-1, 3), (0, 2)], res)
        self.assertTrue(SumOfTwo.find_pairs(ints, 10) == [])

    def test_find_sum_of_three_positive(self):
        ints = [3, 0, -1, 2, 1, 2, 0]
        ints = sorted(ints)  # [-1, 0, 0, 1, 2, 2, 3])
        res = SumOfThree.find_triplets(ints, target=3)
        self.assertEqual([(-1, 1, 3), (-1, 2, 2), (0, 0, 3), (0, 1, 2)], res)
        self.assertEqual(SumOfThree.find_triplets(ints, target=10), [])

    def test_find_sum_of_three_large_set(self):
        ints = []
        for i in range(int(math.pow(2, 10))):
            ints.append(random.randint(-1000, 1000))
        ints = sorted(ints)
        target = random.randint(-1000, 1000)
        res = SumOfThree.find_triplets(ints, target)
        print(f"TARGET = {target}\n TRIPLETS = ")
        for r in res:
            print(r)
        self.assertTrue(res is not None)
