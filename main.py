from print_board import print_board
from win_checker import win_checker
from create_board import create_board
from human_turn import human_turn
from end_game_message import end_game_message
from computer_turn import computer_turn

def new_game():
    while True:
        board: list[list[str]] = create_board()
        win: bool = False
        turn: int = 0
            
        while win == False and turn < len(board) ** 2:
            if turn % 2 == 0:
                board = human_turn(board)
            else:
                computer_turn(board)

            win = win_checker(board, turn)
            turn += 1
            
        if end_game_message(board, win, turn):
            break

new_game()
