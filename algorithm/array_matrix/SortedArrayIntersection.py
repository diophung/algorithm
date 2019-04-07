# FB initial
# Find Intersection of sorted arrays
#
# Input:
# a = [1, 3, 5, 6, 10, 12,... 10000000]
# b = [0, 3, 4, 10, 11]
# Output: [3, 10]
from math import log


def bin_search(e, elements, left, right):
    """ return index of e in elements, -1 if not found"""
    while left <= right:
        mid = (left + right) / 2
        if elements[mid] == e:
            return mid
        elif elements[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def get_intersection_bs(smaller, larger):
    """Get intersection using binary search"""
    output = []
    for e in smaller:
        if bin_search(e, larger, 0, len(larger)) != -1:
            output.append(e)

    return output


def get_intersection_linear(list1, list2):
    output = []
    len1, len2 = len(list1), len(list2)
    i1, i2 = 0, 0
    while i1 < len1 and i2 < len2:
        if list1[i1] < list2[i2]:
            i1 += 1
        elif list2[i2] < list1[i1]:
            i2 += 1
        else:
            output.append(list1[i1])
            i1 += 1
            i2 += 1

    return output


class FindStrategy():
    def __init__(self):
        pass

    RATIO = 0.99

    @staticmethod
    def get_intersection(list1, list2):
        # find strategy based on size of list1 , list2
        a, b = len(list1), len(list2)
        linear = a + b
        bs = min(b * log(a), a * log(b))
        which = min(linear, bs)
        if which == linear:
            print('linear')
        else:
            print('bs')


lst = [1, 2, 50, 61, 100]
l1 = [1, 3, 5, 10, 11, 30]
l2 = [2, 5, 10, 20, 21, 30]

l1 = [x + 1 for x in range(1, 10000000)]
l2 = [x + 2 for x in range(1, 20000000)]
print(FindStrategy.get_intersection(l1, l2))
