from world import GameBoard
from random import randint


class AgentOrange:
    def __init__(self):
        self.current_board = GameBoard()
        self.place_location = list()

    def assess(self, board):
        self.current_board = board
        if self.current_board.get_mark(1, 1) == 'e':
            return 1, 1
        elif self.current_board.winner != 'none':
            return self.place_location[0], self.place_location[1]
        elif self.check('x'):
            return self.place_location[0], self.place_location[1]
        elif self.check('o'):
            return self.place_location[0], self.place_location[1]
        else:
            self.place_location = self.random_placement()
            return self.place_location[0], self.place_location[1]

    def check(self, key):
        for x in range(0, 3):
            for y in range(0, 3):
                if self.current_board.get_mark(x, y) == key:
                    if x < 2:
                        if self.current_board.get_mark(self.right(x), y) == key:
                            if x == 0 and self.current_board.is_empty(2, y):
                                self.place_location = [2, y]
                                return True
                            if x == 1 and self.current_board.is_empty(0, y):
                                self.place_location = [0, y]
                                return True
                    if x > 0:
                        if self.current_board.get_mark(self.left(x), y) == key:
                            if x == 1 and self.current_board.is_empty(2, y):
                                self.place_location = [2, y]
                                return True
                            if x == 2 and self.current_board.is_empty(0, y):
                                self.place_location = [0, y]
                                return True
                    if y < 2:
                        if self.current_board.get_mark(x, self.down(y)) == key:
                            if y == 0 and self.current_board.is_empty(x, 2):
                                self.place_location = [x, 2]
                                return True
                            if y == 1 and self.current_board.is_empty(x, 0):
                                self.place_location = [x, 0]
                                return True
                    if y > 0:
                        if self.current_board.get_mark(x, self.up(y)) == key:
                            if y == 1 and self.current_board.is_empty(x, 2):
                                self.place_location = [x, 2]
                                return True
                            if y == 2 and self.current_board.is_empty(x, 0):
                                self.place_location = [x, 0]
                                return True
                    if x == 1 and y == 1:
                        if self.current_board.get_mark(self.right(x), self.down(y)) == key:
                            if self.current_board.is_empty(0, 0):
                                self.place_location = [0, 0]
                                return True
                        if self.current_board.get_mark(self.right(x), self.up(y)) == key:
                            if self.current_board.is_empty(0, 2):
                                self.place_location = [0, 2]
                                return True
                        if self.current_board.get_mark(self.left(x), self.down(y)) == key:
                            if self.current_board.is_empty(2, 0):
                                self.place_location = [2, 0]
                                return True
                        if self.current_board.get_mark(self.left(x), self.up(y)) == key:
                            if self.current_board.is_empty(2, 2):
                                self.place_location = [2, 2]
                                return True
        return False

    def random_placement(self):
        x = randint(0, 2)
        y = randint(0, 2)
        while self.current_board.is_empty(x, y) == False:
            x = randint(0, 2)
            y = randint(0, 2)
        return [x, y]

    def left(self, x):
        return x - 1

    def right(self, x):
        return x + 1

    def up(self, y):
        return y - 1

    def down(self, y):
        return y + 1
