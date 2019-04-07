"""
Merge intervals and return the non-overlapping ones
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class MergeInterval(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals = sorted(intervals, key=lambda i: i.start)
        for i in range(len(intervals)):
            # mergeable, no overlap
            if res and intervals[i].start >= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res


sol = MergeInterval()
intervals = [Interval(5, 8), Interval(6, 8)]
print([intervals, sol.merge(intervals)])

intervals = [Interval(9, 10), Interval(4, 9), Interval(4, 17)]
print([intervals, sol.merge(intervals)])
