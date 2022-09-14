"""
Problem:
    A frog can jump 1,2,3...N stairs at a time. Find the number of ways it can jump to the exact N-th stair.

Solution:
    This is partition problem in number theory : https://en.wikipedia.org/wiki/Partition_(number_theory)
    However, the solution presented here is a much simpler version.

    We see these N stairs as a series of stairs ([S])
    For e.g: 4 stairs are represented as:

                                         __stop__[Stair]
                          __stop__[Stair]
           __stop__[Stair]
    [Stair]

    The number of ways to jump these N stairs, is the number of ways to stop in between stairs.
    There are N-1 stops between these stairs.
    To use a stop, we mark it as "1". Otherwise, we mark it as "0". For e.g: (2,2) is represented as "010", (1,3) is "100"
    Now the original problem is equivalent to: how many unique strings we can build using N-1 characters '1' and '0'.

    It is like binary system, so the answer is: 2^(N-1).
"""


def count_frog_jump(n):
    if n <= 0:
        raise ValueError("N must be positive")
    return pow(2, n - 1)

print(PartitionOfIntegerAsSum.solve(1))  # 1 way, = (1)
print(PartitionOfIntegerAsSum.solve(2))  # 2 ways, = (1,1), (2)
print(PartitionOfIntegerAsSum.solve(3))  # 4 ways, = (1,1,1), (1,2), (2,1), (3)
print(PartitionOfIntegerAsSum.solve(4))  # 8 ways, = (1,1,1,1), (1,1,2), (1,2,1), (1,3), (2,2), (2,1,1), (3,1), (4)
print(PartitionOfIntegerAsSum.solve(60))  # oh dear
