import unittest
import sys

from algo.array_matrix.BattleshipInABoard import BattleshipInBoard


class TestBattleShipInABoard(unittest.TestCase):

    def test_positive_case(self):
        s = BattleshipInBoard()
        board = [
            "...X",
            "X..X",
            "...X",
        ]
        self.assertEqual(s.count_ship(board), 2)
        ################
        board = [
            "...X",
            "XX.X",
            "...X",
        ]
        self.assertEqual(s.count_ship(board), 2)
        ################
        board = [
            "...X",
            "....",
            "XX.X",
        ]
        self.assertEqual(s.count_ship(board), 3)
        ################
        board = [
            "...X",
            "....",
            "....",
        ]
        self.assertEqual(s.count_ship(board), 1)
        ################
        board = [
            "....",
            "....",
            "....",
        ]
        self.assertEqual(s.count_ship(board), 0)
