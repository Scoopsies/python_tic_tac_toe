from win_checker import win_checker
from human_turn import update_board
from available_moves import available_moves
from custom_types import Board


def computer_turn(board: Board):
    available = available_moves(board)
    computer_choice = str(available[0])
    miniMax(board, available)
    return update_board(board, computer_choice, available)
    

def miniMax(board: Board, available_moves):
    print(available_moves)



