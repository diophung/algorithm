"""
LeetCode 419:
Given an 2D board, count how many battleships are in it.
The battleships are represented with 'X's, empty slots are represented with '.'s.

You may assume the following rules:
- You receive a valid board, made of only battleships or empty slots.
- Battleships can only be placed horizontally or vertically.
In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
- At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

Example:
    X..X
    ...X
    ...X
In the above board there are 2 battleships.

Invalid Example:
    ...X
    XXXX
    ...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""


class BattleshipInBoard:
    def __init__(self):
        pass

    @staticmethod
    def count_ship(board):
        ship_count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                # water
                if board[i][j] == '.':
                    continue
                # count the ship using only the top-left pixel
                if board[i][j] == 'X':
                    # horizontal ship
                    if i > 0 and board[i - 1][j] == 'X':
                        continue
                    # vertical ship
                    if j > 0 and board[i][j - 1] == 'X':
                        continue
                    ship_count += 1
        return ship_count
