"""
problem: a frog can jump 1,2,3...n steps at a time. How many way it can jump exactly N-step
count_jump(1) = (1) = 1
count_jump(2) = (1,1), (2) = 2
count_jump(3) = (1,1,1), (1,2), (2,1), (3) = 4
count_jump(4) = (1,1,1,1), (1,1,2), (1,2,1), (1,3), (2,1,1), (2,2), (3,1), (4) = 8
"""
import math


class FrogJump:
    @staticmethod
    def count_jump(N):
        """
        Look at the empty spaces ( _ ) between the steps: | _ | _ | _ |
            The number of ways to jump is the way to pick which space to stop.
            Given N step, there are (N-1) space.
            Imagine each space is a bit, the problem now is  : how many unique number can be represent by N-1 bits
            N-1 bit can represent 2^(N-1) numbers.
        """
        ways = int(math.pow(2, N - 1))
        print('Given %s steps, there are %s ways' % (N, ways))


FrogJump.count_jump(1)  # expect 1
FrogJump.count_jump(2)  # expect 2
