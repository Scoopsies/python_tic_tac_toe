from win_checker import win_checker
from create_board import create_board
from human_turn import human_turn
from computer_turn import computer_turn
from board_type import Board
from play_again_prompt import play_again_prompt
from available_moves import available_moves
from print_board import print_board

def new_game():
    while True:
        board: Board = create_board()
        win_message = 'No Winners.'
        available_spaces = available_moves(board)
  
            
        while win_message == 'No Winners.' and len(available_spaces):
            turn = len(board) ** 2 - len(available_spaces)
            print(f'available spaces: {available_spaces}')
            print(f'turn: {turn}')
            if turn % 2 == 0:
                board = human_turn(board, available_spaces)
            else:
                board = computer_turn(board, available_spaces)

            win_message = win_checker(board, available_spaces)
            available_spaces = available_moves(board)
            
        print_board(board)   
        print(win_message)
        if play_again_prompt():
            break

new_game()