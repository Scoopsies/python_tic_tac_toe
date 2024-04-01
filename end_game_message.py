from print_board import print_board
from play_again_prompt import play_again_prompt
from custom_types import Board

def end_game_message(board: Board, win: str, turn: int) -> bool:
    print_board(board)
    if win == 'no winner':
        print('Draw')
    else:
        print(win)

    return play_again_prompt()