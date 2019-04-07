# Problem: given 2D matrix filled with 1s. There is a rectangle inside that 2D
# matrix filled with 0s. Write a function to return the coordinate of
# top-left and bottom-right of that rectangle


def get_rectangle_post(mat):
    R, C = len(mat), len(mat[0])
    for r in range(R):
        for c in range(C):
            # found top-left
            if mat[r][c] == 0:
                end_r, end_c = r, c
                # move down till "1"
                while end_r < R and mat[end_r][c] == 0:
                    end_r += 1

                # move right till "1"
                while end_c < C and mat[r][end_c] == 0:
                    end_c += 1

                # found bottom-right
                return r, c, end_r - 1, end_c - 1
    return -1, -1, -1, -1


matrix = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0]
]

print(get_rectangle_post(matrix))  # [2,2,4,4]

matrix = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
]
print(get_rectangle_post(matrix))  # [2,1,3,3]

matrix = [
    [1, 1],
    [1, 0]
]
print(get_rectangle_post(matrix))  # [1,1,1,1]

matrix = [[0]]
print(get_rectangle_post(matrix))  # [0,0,0,0]

matrix = [[1]]
print(get_rectangle_post(matrix))  # [-1, -1, -1, -1]
