class GameBoard:
    def __init__(self):
        self.column = list()
        self.used = int()
        self.winner = str()
        self.build_board()
        self.game_tie = bool()

    def build_board(self):
        self.column = [['e', 'e', 'e'], ['e', 'e', 'e'], ['e', 'e', 'e']]
        self.used = 0
        self.winner = 'none'

    def print_board(self):
        for i in range(0, 3):
            print(self.column[i][0], self.column[i][1], self.column[i][2])
        print('')

    def get_mark(self, x, y):
        return self.column[y][x]

    def game_over(self):
        for i in range(0, 3):
            if all(item == 'x' for item in self.column[i]):
                self.winner = 'x'
            if all(item == 'o' for item in self.column[i]):
                self.winner = 'o'
            if self.get_mark(i, 0) == self.get_mark(i, 1) and self.get_mark(i, 1) == self.get_mark(i, 2) \
                    and self.get_mark(i, 0) != 'e':
                self.winner = self.get_mark(i, 0)
        if self.column[0][0] == self.column[1][1] and self.column[1][1] == self.column[2][2]:
            self.winner = self.column[0][0]
        if self.column[2][0] == self.column[1][1] and self.column[1][1] == self.column[0][2]:
            self.winner = self.column[2][0]
        self.game_tie = True
        for u in range(0, 3):
            for k in range(0, 3):
                if self.get_mark(u, k) == 'e':
                    self.game_tie = False
                    continue
        if self.game_tie and self.winner == 'none':
            self.winner = 'tie'

    def set_mark(self, player, r, c):
        self.column[c][r] = player
        self.game_over()


    def is_empty(self, x_val, y_val):
        if self.get_mark(x_val, y_val) == 'e':
            return True
        else:
            return False