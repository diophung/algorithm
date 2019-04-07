#!/usr/bin/python3
import itertools
import os
import multiprocessing
import sys
import time
from nltk.corpus import stopwords

# pip install nltk
STOP_WORDS = set(stopwords.words('english'))
TOKENIZER = " "
ITEMS_PER_SUBLIST = 100000
LINES_PER_FILE = 50000
SPLITTED_FILE_PREFIX = "splitted_"


class MapReduceTask(object):

    def __init__(self, mapper, reducer):
        self.mapper = mapper
        self.reducer = reducer
        self.pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    def partition(self, keyvalue_items):
        # partitioning items by the key (i.e the word itself)
        partitions = {}
        for key, value in keyvalue_items:
            try:
                partitions[key].append(value)
            except KeyError:
                partitions[key] = [value]
        return partitions.items()

    def process(self, inputs):
        # a simple demo for using map/reduce on local machine. For large data, we can use M/R on Hadoop
        mapped_data = self.pool.map(self.mapper, inputs)
        partitioned_data = self.partition(itertools.chain(*mapped_data))
        reduced_data = self.pool.map(self.reducer, partitioned_data)
        return reduced_data


def split_file(file_path):
    # in case file too big for memory, split into smaller pieces and copied to different servers
    cmd = "split -l %d %s %s".format(LINES_PER_FILE, file_path, SPLITTED_FILE_PREFIX)
    os.system(cmd)


def split_list(list):
    # split a list into smaller chunks
    for i in xrange(0, len(list), ITEMS_PER_SUBLIST):
        yield list[i: i + ITEMS_PER_SUBLIST]


def map(words):
    # map function, produce the mapped data in the format of ("text", 1)
    mapped = []
    for w in words:
        if w.isalpha() and w.lower() not in STOP_WORDS and w not in STOP_WORDS:
            mapped.append((w, 1))
    return mapped


def reduce(partition):
    # reduce function by summing up the count of each word.
    # each partition is in the form of ("text", [1,1,1,...1])
    word, count = partition
    return (word, sum(count))


def read(fpath):
    # for large file, consider split_file() first, then works on smaller trunks
    with open(fpath, "r") as file:
        lines = file.readlines()
    return (''.join(lines)).split()


def tuple_sort(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return cmp(a[0], b[0])


def run(fpath):
    if fpath is None:
        print("Please enter a path")
        sys.exit(1)

    start = time.time()
    text = read(fpath)
    raw_data = list(split_list(text))

    map_reduce = MapReduceTask(map, reduce)
    results = map_reduce.process(raw_data)
    results.sort(tuple_sort)

    print('Top 20 frequent words:')
    for key, value in results[:20]:
        print(key, value)
    print('total unique words: ' + str(len(results)))
    end = time.time() - start
    print('took: ' + str(end) + 's')


# run(sys.argv[1])
print('Analyzing Shakespeare''s works')
run('./data/sp.txt')
