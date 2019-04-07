"""
1*21000
23*1011
*21101*
2100011
"""
import random


class MineSweeper:
    def __init__(self, rows, columns, number_of_mines):
        self.rows = rows
        self.columns = columns
        self.number_of_mines = number_of_mines
        self.mine_locations = [(0, 0)] * number_of_mines
        self.board = [[0] * columns for y in range(rows)]
        self.generate_board(rows, columns, number_of_mines)

    def is_a_mine(self, x, y):
        return self.is_valid_location(self.rows, self.columns, x, y) and self.board[x][y] == '*'

    def mark_nearby_cells(self, bomb_x, bomb_y):
        # up,down,left,right and 4 diagonal directions.
        nav_x = [-1, 0, 1, 1, 1, 0, -1, -1]
        nav_y = [1, 1, 1, 0, -1, -1, -1, 0]
        for step in range(8):
            nearby_x = bomb_x + nav_x[step]
            nearby_y = bomb_y + nav_y[step]
            # don't update a bomb
            if not self.is_a_mine(nearby_x, nearby_y):
                if self.is_valid_location(self.rows, self.columns, nearby_x, nearby_y):
                    self.board[nearby_x][nearby_y] += 1

    def is_valid_location(self, max_rows, max_columns, row, col):
        return 0 <= row < max_rows and 0 <= col < max_columns

    def generate_board(self, rows, columns, number_of_mines):
        while number_of_mines > 1:
            x = random.randint(0, rows - 1)
            y = random.randint(0, columns - 1)
            if (x, y) not in self.mine_locations:
                self.mine_locations.append((x, y))
                number_of_mines -= 1

        for loc in self.mine_locations:
            x = loc[0]
            y = loc[1]
            self.board[x][y] = '*'

        for r in range(rows):
            for c in range(columns):
                if self.is_a_mine(r, c):
                    self.mark_nearby_cells(r, c)

    def print_board(self):
        for r in range(self.rows):
            for c in range(self.columns):
                print(self.board[r][c])

game = MineSweeper(7, 7, 7)
game.print_board()
