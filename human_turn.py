from print_board import print_board
from available_moves import available_moves
from update_board import update_board
from custom_types import Board




def human_turn(board: Board) -> Board:
    print_board(board)
    player_choice = input(f'Please select a spot. (1 - {len(board) ** 2})\n \n')
    available = available_moves(board)
    updated_board = update_board(board, player_choice, available)
    return updated_board

