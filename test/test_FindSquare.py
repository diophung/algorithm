
class FindSquareTest(unittest.TestCase):

    def test_find_square(self):
        lst1 = [1, 2, 3, 4, 5, 6]
        lst2 = [4, 9, 16, 64]

        self.assertEqual(FindSquareSoln.find_square(lst1, lst2), [2, 3, 4])
