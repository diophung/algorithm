import random
import bitarray
import math


class BloomFilter:
    """
    Guarantee not-in-the-list to be 100% correct. In-the-list maybe false positive.
    Using multiple hash functions to mark the bit in the bit-array_matrix to indicate
    """
    def __init__(self, max_items, false_positive_rate):
        """
        Create a Bloom filter
        :param max_items: the maximum items to be used with this filter.
        :param false_positive_rate: expected is-in-the-set false positive rate.
        """

        self.num_of_bit = math.log(max_items)
        self.bit_array = bitarray(self.num_of_bit)
        self.hash_func = []

    def add(self, item):
        for h in self.hash_func:
            h(item)
        print('added')

    def contains(self, item):
        """
        Check if this string is in the element
        """
        rand = random.randint(1, 2)
        print(rand)


filter = BloomFilter(2, 0.99)
filter.add('1')
filter.add('1')
filter.add('2')
filter.add('11')
filter.add('122')
filter.add('1')
