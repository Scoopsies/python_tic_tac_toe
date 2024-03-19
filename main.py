from print_board import print_board
from win_checker import win_checker

def new_game():
    board = [
        ['1','2','3'], 
        ['4','5','6'],
        ['7','8','9']
    ]
    win = False
    
    while win == False:
        print_board(board)
        player_choice = int(input('Where do you want to play? \n \n')) - 1
        y_axis = int((player_choice)/ 3)
        x_axis = player_choice % 3
        board[y_axis][x_axis] = 'X'
        win = win_checker(board)

    print_board(board)
    print('You Win!')

    

new_game()