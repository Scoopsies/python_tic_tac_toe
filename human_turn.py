from print_board import print_board
from available_moves import available_moves
from update_board import update_board
from board_type import Board




def human_turn(board: Board, available_spaces: list[int]) -> Board:
    print_board(board)
    player_choice = input(f'Please select a spot. (1 - {len(board) ** 2})\n \n')
    updated_board = update_board(board, player_choice, available_spaces)
    return updated_board

