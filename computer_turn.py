from win_checker import win_checker
from human_turn import update_board
from board_type import Board

def computer_turn(board: Board, available_moves):
    computer_choice = str(available_moves[0])
    return update_board(board, computer_choice, available_moves)
