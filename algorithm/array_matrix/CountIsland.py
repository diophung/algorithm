import unittest


class CountIsland(object):
    # Given a 2D array of 1s and 0s, count the number of "islands of 1s" (groups of connecting 1s)
    # For example, given:
    # [
    #  [1, 1, 0, 0, 0],
    #  [0, 1, 0, 0, 1],
    #  [1, 0, 0, 1, 1],
    #  [0, 0, 0, 0, 0],
    #  [1, 0, 1, 0, 1]
    # ]

    # Output = 6

    # algo :
    # 1. start with any location
    # 2. go up down left right, check if it still land
    # 3. at the same time: remember if it's visited
    # 4. then scan the whole grid,
    #     for each piece of land, do this BFS
    #     then increase island count +1

    @staticmethod
    def is_in_grid(r, c, grid):
        return 0 <= r < len(grid) \
               and 0 <= c < len(grid[0])

    def island_count(self, grid):
        """
        count without changing the grid
        """
        count = 0
        # UP, DOWN, LEFT, RIGHT
        col_nav = [1, -1, 0, 0]
        row_nav = [0, 0, 1, -1]
        nodes = []
        visited = set()

        def search(r, c):
            nodes.append((r, c))
            visited.add((r, c))
            while len(nodes) != 0:
                curr = nodes.pop()
                curr_r = curr[0]
                curr_c = curr[1]
                for i in range(4):  # try all 4 directions
                    next_r = curr_r + col_nav[i]
                    next_c = curr_c + row_nav[i]
                    # if it's a valid piece of land
                    # and not yet visited
                    # then mark as visited, and BFS from there
                    if self.is_in_grid(next_r, next_c, grid) \
                            and grid[next_r][next_c] == 1 \
                            and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        nodes.append((next_r, next_c))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    search(r, c)
                    count += 1
        return count

    def island_count_inplace(self, grid):
        count = 0
        visited = set()
        nodes = []
        while len(nodes) > 0:
            nodes.append((0, 0))
            curr = nodes.pop()
        return count


class CountIslandTest(unittest.TestCase):

    def test_positive_case(self):
        ci = CountIsland()
        grid1 = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        grid2 = [
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1]
        ]
        grid3 = [
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]
        grid4 = [
            [0, 0, 0, 0, 0],
        ]
        self.assertEquals(ci.island_count(grid1), 6)
        self.assertEquals(ci.island_count(grid2), 2)
        self.assertEquals(ci.island_count(grid3), 1)
        self.assertEquals(ci.island_count(grid4), 0)
