import unittest


class JeepDrone:
    _nav_map = []
    x_dir = [0, 0, -1, 1, -1, 1, -1, 1]
    y_dir = [-1, 1, 0, 0, -1, -1, 1, 1]

    def __init__(self, nav_map=None):
        self._nav_map = nav_map
        self.R = len(nav_map)
        self.C = len(nav_map[0])

    def navigate_to_extraction_point(self, current):
        """ return the coordinate of the first extraction point
        params:
            start: ()
            nav_map: []
        """
        found = False
        while not found:
            if self.is_extract_point(current):
                return current
            else:
                neighbors = self.get_neighbors(current)
                highest = self.get_highest_points(neighbors)
                current = highest

    def height(self, point):
        return self._nav_map[point[1]][point[0]]

    def is_extract_point(self, point):
        neighbors = self.get_neighbors(point)
        for n in neighbors:
            if self.height(point) < self.height(n):
                return False
        return True

    def get_highest_points(self, points):
        highest = -1
        point = None
        for p in points:
            if self.height(p) >= highest:
                highest = self.height(p)
                point = p
        return point

    def get_neighbors(self, point):
        neighbors = []
        for i in range(8):
            new_point = self.navigate(point, self.x_dir[i], self.y_dir[i])
            if self.is_in_map(new_point):
                neighbors.append(new_point)
        return neighbors

    def is_in_map(self, point):
        return 0 <= point[0] < self.C and 0 <= point[1] < self.R

    @staticmethod
    def navigate(point, x, y):
        # UP, DOWN, LEFT, RIGHT, TOP-LEFT
        return point[0] + x, point[1] + y


class JeepDroneTest(unittest.TestCase):

    def test_nav_laser_positive_case(self):
        nav_map = [
            # x
            [1, 1, 1, 1, 1, 1, 1],  # y
            [1, 2, 3, 1, 1, 2, 4],  #
            [1, 2, 4, 2, 1, 2, 2],
            [1, 2, 5, 2, 1, 1, 1],
            [1, 1, 2, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 2],
        ]
        jeep = JeepDrone(nav_map)
        self.assertEquals(jeep.navigate_to_extraction_point((0, 0)), (2, 3))
        self.assertEquals(jeep.navigate_to_extraction_point((6, 5)), (6, 5))
        self.assertEquals(jeep.navigate_to_extraction_point((3, 4)), (2, 3))


if __name__ == "__main__":
    unittest.main()
