
import unittest


class JeepDrone:
    _nav_map = []
    # navigation: up down left right, 2 diagonal dir
    X_DIR = [0, 0, -1, 1, -1, 1, -1, 1]
    Y_DIR = [-1, 1, 0, 0, -1, -1, 1, 1]

    def __init__(self, nav_map=None):
        self._nav_map = nav_map
        self.ROW_SIZE = len(nav_map)
        self.COL_SIZE = len(nav_map[0])

    def navigate_to_extraction_point(self, starting_point):
        """
        Return the coordinate of the first extraction point

        Args:
            starting_point: ()


        """
        found = False
        while not found:
            if self.is_extract_point(starting_point):
                return starting_point
            else:
                neighbors = self.get_neighbors(starting_point)
                highest = self.get_highest_points(neighbors)
                starting_point = highest

    def get_height(self, point):
        return self._nav_map[point[1]][point[0]]

    def is_extract_point(self, point):
        neighbors = self.get_neighbors(point)
        for n in neighbors:
            if self.get_height(point) < self.get_height(n):
                return False
        return True

    def get_highest_points(self, points):
        highest = -1
        point = None
        for p in points:
            if self.get_height(p) >= highest:
                highest = self.get_height(p)
                point = p
        return point

    def get_neighbors(self, curr_loc):
        """
        Return all surrounding locations.
        Args:
            curr_loc (tuple): (x, y) represent a location in the map

        Returns:
            list[tuple]
        """
        neighbors = []
        for i in range(8):
            new_loc = JeepDrone.navigate(curr_loc, self.X_DIR[i], self.Y_DIR[i])
            if self.is_in_map(new_loc):
                neighbors.append(new_loc)
        return neighbors

    def is_in_map(self, point):
        return 0 <= point[0] < self.COL_SIZE and 0 <= point[1] < self.ROW_SIZE

    @staticmethod
    def navigate(point, x, y):
        """
        Move from a point to another point,
        Args:
            point (tuple): the location
            x (int): change in x-axis
            y (int): change in y-axis

        Returns:
            new tuple representing the new location

        """
        # UP, DOWN, LEFT, RIGHT, TOP-LEFT
        return point[0] + x, point[1] + y


class JeepDroneTest(unittest.TestCase):

    def test_nav_laser_positive_case(self):
        nav_map = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 2, 3, 1, 1, 2, 4],
            [1, 2, 4, 2, 1, 2, 2],
            [1, 2, 5, 2, 1, 1, 1],
            [1, 1, 2, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 2],
        ]
        jeep = JeepDrone(nav_map)
        self.assertEqual(jeep.navigate_to_extraction_point((0, 0)), (2, 3))
        self.assertEqual(jeep.navigate_to_extraction_point((6, 5)), (6, 5))
        self.assertEqual(jeep.navigate_to_extraction_point((3, 4)), (2, 3))


if __name__ == "__main__":
    unittest.main()
