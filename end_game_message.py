from print_board import print_board
from play_again_prompt import play_again_prompt

def end_game_message(board: list[list[str]], win: bool, turn: int) -> bool:
    print_board(board)
    if not win and turn >= len(board) ** 2:
        print('Draw')
    elif turn % 2:
        print('You Win!')
    else:
        print('You Lose')

    return play_again_prompt()