from bitarray import bitarray
from random import shuffle

import math
import mmh3


class BloomFilter:
    """
    To tell if an item is DEFINITELY NOT IN, or PROBABLY IN a set.     
    Use a bit array : K[], and hash function H
    to insert element X: H(X) N times, where N is number of time to hash

    to check set membership: hash and compute the digest in bit array
        if any of them false --> for sure not in the set
    
    assumption1: using  uniform non-cryptographic hash function (fast hash)
    assumption2: false positive is possible, false negative is not

    """

    def __init__(self, item_count, fp_prob):
        """
        item_count: int , size of bloom filter
        false_positive_prob: float, chance of telling an item is in but it is not
        """
        # false positive probability in decimal
        self.fp_prob = fp_prob

        self.bit_arr_size = self.get_bit_arr_size(item_count, fp_prob)

        # how many time to use the hash function
        self.hash_count = self.get_hash_count(self.bit_arr_size, item_count)

        # bit array to use as filter, checking set membership
        self.bit_array = bitarray(self.bit_arr_size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def insert(self, item):
        # add an item to the filter so that we can check set membership later
        for i in range(self.hash_count):
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.bit_arr_size
            # set the bit True in bit_array
            self.bit_array[digest] = True

    def check(self, item):
        # can return false positive when, as more element added to the filter
        # the fix: increase bit array size and number of times to hash
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.bit_arr_size
            if not self.bit_array[digest]:
                # if any of bit is False then,it's not present in filter
                # else there is a chance it exists
                return False
        return True

    def get_bit_arr_size(self, item_count, fp_prob):
        """
        Return the size of bit array(m) using following formula
        m = -(n * log(p)) / (log(2)^2)
        item_count : int
            number of items expected to be stored in filter
        fp_prob : float
            False Positive probability in decimal
        """
        m = -(item_count * math.log(fp_prob)) / (math.log(2) ** 2)
        return int(m)

    def get_hash_count(self, bit_arr_size, item_count):
        """
        Return the hash function count k, using following formula
        k = (m/n) * log(2)
  
        bit_arr_size : int
            size of bit array
        item_count : int
            number of items expected to be stored in filter
        """
        k = (bit_arr_size / item_count) * math.log(2)
        return int(k)


def test_bloom_filter():
    item_count = 100000000  # 100M items
    fp_prob = 0.00001  # 0.001%, i.e 99.99% BF is correct
    bloomf = BloomFilter(item_count, fp_prob)
    # bit array size ~ 300MB
    print("size of bit array: {}".format(bloomf.bit_arr_size))
    print("false positive prob: {}".format(bloomf.fp_prob))
    print("hash count: {}".format(bloomf.hash_count))

    words = ["Lorem", "ipsum", "dolor", "sit", "amet,", "consectetuer", "adipiscing",
             "elit.", "Maecenas", "porttitor", "congue", "massa.",
             "Fusce", "posuere,", "magna", "sed", "pulvinar", "ultricies,",
             "purus", "lectus", "malesuada", "libero,", "sit", "amet",
             "commodo", "magna", "eros", "quis", "urna"]

    other_words = ["Bây", "giờ", "cho", "phim", "hoạt", "hình.", "Đó", "là", "lâm", "sàng.",
                   "Chúng", "ta", "đang", "sống", "trên", "trái", "đất."]

    for w in words:
        bloomf.insert(w)

    shuffle(words)
    shuffle(other_words)

    random_words = words[:20] + other_words
    shuffle(random_words)

    for w in random_words:
        if bloomf.check(w):
            if w in other_words:
                print("`{}` : FALSE POSITIVE".format(w))
            else:
                print("`{}` probably in {}".format(w, words))
        else:
            print("`{}` DEFINITELY not in {}".format(w, words))


if __name__ == "__main__":
    test_bloom_filter()