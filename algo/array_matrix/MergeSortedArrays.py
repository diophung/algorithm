import unittest


class MergeSortedArray(object):

    @staticmethod
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int] with the size of m + n (with the last n elements are initially 0)
        :type m: the first m elements in nums1
        :type nums2: List[int]
        :type n: int, the length of nums2
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # [1, 2, 3, 0, 0 ]
        # [4, 6]

        ni = n - 1
        mi = m - 1
        for d in range(n + m - 1, -1, -1):
            # if no more to merge
            if ni < 0:
                return

            # store larger number
            if nums1[mi] < nums2[ni]:
                nums1[d] = nums2[ni]
                ni = ni - 1
            else:
                nums1[d] = nums1[mi]
                mi = mi - 1


class MergeSortedArrayTest(unittest.TestCase):

    def test_merge(self):
        nums1 = [1, 2, 3, 0, 0]
        nums2 = [5, 6]
        MergeSortedArray.merge(nums1, 3, nums2, 2)
        self.assertEquals(nums1, [1, 2, 3, 5, 6])

    def test_merge_alternative(self):
        nums1 = [1, 9, 0, 0, 0, 0]
        nums2 = [5, 6, 7, 8]
        MergeSortedArray.merge(nums1, 2, nums2, 4)
        self.assertEquals(nums1, [1, 5, 6, 7, 8, 9])
