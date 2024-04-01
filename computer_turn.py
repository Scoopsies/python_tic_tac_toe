from win_checker import win_checker
from human_turn import update_board
from available_moves import available_moves
from custom_types import Board
import math

def computer_turn(board: Board):
    available = available_moves(board)
    computer_choice = str(available[0])
    return update_board(board, computer_choice, available)
