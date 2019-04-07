import unittest

from algorithm.array_matrix.BattleshipInABoard import BattleshipInBoard


class TestBattleShipInABoard(unittest.TestCase):
    
    def test_positive_case(self):
        s = BattleshipInBoard()
        board = [
            "...X",
            "X..X",
            "...X",
        ]
        self.assertEquals(s.count_ship(board), 2)
        ################
        board = [
            "...X",
            "XX.X",
            "...X",
        ]
        self.assertEquals(s.count_ship(board), 2)
        ################
        board = [
            "...X",
            "....",
            "XX.X",
        ]
        self.assertEquals(s.count_ship(board), 3)
        ################
        board = [
            "...X",
            "....",
            "....",
        ]
        self.assertEquals(s.count_ship(board), 1)
        ################
        board = [
            "....",
            "....",
            "....",
        ]
        self.assertEquals(s.count_ship(board), 0)
