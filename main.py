from world import GameBoard
from AgentOrange import AgentOrange as O
from AgentX import AgentX as X

w = GameBoard()
player_x = X()
player_o = O()

while w.winner == 'none':
    x, y = player_x.assess(w)
    w.set_mark('x', x, y)
    w.print_board()
    x, y = player_o.assess(w)
    w.set_mark('o', x, y)
    w.print_board()
print('Winner is: ', w.winner)
