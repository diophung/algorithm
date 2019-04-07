# Problem: a frog want to jump from X to Y,
# each jump it can move a distance D.
# Count the number of required jumps so that the frog can get to or past Y.

import math


def FrogJump(start_pos, end_pos, jump_size):
    return int(math.ceil(float(end_pos - start_pos) / float(jump_size)))


print(FrogJump(10, 80, 30))  # expect 3
