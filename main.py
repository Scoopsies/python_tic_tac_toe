from print_board import print_board
from win_checker import win_checker
from create_board import create_board
from human_turn import human_turn

def new_game():
    while True:
        board: list[list[str]] = create_board()
        board_length: int = len(board)
        win: bool = False
        turn: int = 0

        def computerTurn(board):
            print('computer')
        
        while win == False and turn < board_length ** 2:
            if turn % 2 == 0:
                board = human_turn(board)
                win = win_checker(board)
                turn += 1
            else:
                print('computer')
                turn += 1
            
        print_board(board)
        print('You Win!')
        if ('n' == input('Would you like to play again? Y/N \n').lower()):
            break

new_game()
