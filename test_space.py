import tictactoe as ttt
X = "X"
O = "O"
EMPTY = None
state = [[X, X, X],
        [EMPTY, O, EMPTY],
        [O, EMPTY, EMPTY]]
 

 
def winner(board):
    for i in state:
        if all(i):
            print(i.count(i[0]) == len(i))
            
winner(state)
            
'''actions_av = ttt.actions(state)

player = ttt.player(state)

choice = (1, 1)
row = choice[0]
cell = choice[1]

if choice in actions_av:
    state[row][cell] = player
    print(state)'''