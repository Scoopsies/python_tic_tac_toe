from win_checker import win_checker
from create_board import create_board
from human_turn import human_turn
from computer_turn import computer_turn
from custom_types import Board
from play_again_prompt import play_again_prompt

def new_game():
    while True:
        board: Board = create_board()
        win_message = 'No Winners.'
        turn = 0
            
        while win_message == 'No Winners.' and turn < len(board) ** 2:
            if turn % 2 == 0:
                board = human_turn(board)
            else:
                board = computer_turn(board)

            win_message = win_checker(board, turn)
            turn += 1
            
        print(win_message)
        if play_again_prompt():
            break

new_game()