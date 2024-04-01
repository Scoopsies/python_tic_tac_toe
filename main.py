from print_board import print_board
from win_checker import win_checker
from create_board import create_board
from human_turn import human_turn
from end_game_message import end_game_message
from computer_turn import computer_turn
from custom_types import Board

def new_game():
    while True:
        board: Board = create_board()
        win = 'no winner'
        turn = 0
            
        while win == 'no winner' and turn < len(board) ** 2:
            if turn % 2 == 0:
                board = human_turn(board)
            else:
                board = computer_turn(board)

            win = win_checker(board, turn)
            turn += 1
            
        if end_game_message(board, win, turn):
            break

new_game()
