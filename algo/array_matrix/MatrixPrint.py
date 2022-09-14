up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
CLOCKWISE_DIR = [right, down, left, up]
COUNTER_CLOCKWISE_DIR = [down, right, up, left]


def print_matrix_spiral(m, clockwise=True):
    """
    print a M x M matrix in spiral, clockwise, start from top left.
    ---
    m = [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    ]

    print =>
        1, 2, 3, 4
        4, 4, 4,
        3, 2, 1
        1, 1
        2, 3
        3
        2
    """
    M = len(m)
    count = M * M
    visited = [[False for i in range(M)] for j in range(M)]
    curr_dir = 0
    loc = (0, 0)
    prev = loc
    while count > 0:
        x, y = loc[0], loc[1]
        if is_out(m, loc) or visited[x][y]:
            loc = prev  # take 1 step back
            curr_dir = (curr_dir + 1) % 4  # update direction
            loc = move(loc, curr_dir, clockwise)  # move in that direction
            print('')
        else:
            print_loc(m, loc)
            prev = loc
            visited[x][y] = True
            loc = move(loc, curr_dir, clockwise)
            count -= 1


def move(curr, direction, clockwise=True):
    offset = CLOCKWISE_DIR[direction] if clockwise else COUNTER_CLOCKWISE_DIR[direction]
    x = curr[0] + offset[0]
    y = curr[1] + offset[1]
    return x, y


def is_visited(matrix, loc):
    return matrix[loc[0]][loc[1]]


def print_loc(matrix, loc):
    x = loc[0]
    y = loc[1]
    print(matrix[x][y])


def is_out(m, loc):
    return loc[0] < 0 \
           or loc[1] < 0 \
           or loc[0] > len(m) - 1 \
           or loc[1] > len(m) - 1


def find_max_submatrix(m):
    """
    Given a m*n matrix consisting of 0 and 1
    print the sub-matrix with largest number of 1
    """
    pass


def sub_array_sum(m):
    """
    Given a 1-d array_matrix print all the sub-arrays whose elements sum exceed a given value x
    """
    pass


def print_tree_at_level(tree_root, h):
    """
    given tree, print all nodes at given height h
    """
    if h == 0:
        print(tree_root)
    while h > 0:
        for c in h.child_node:
            print_tree_at_level(c, h - 1)


m = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]
print_matrix_spiral(m, clockwise=True)
print_matrix_spiral(m, clockwise=False)
