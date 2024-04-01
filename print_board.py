from custom_types import Board

def print_board(board: Board) -> None:
    board_size = len(board)
    print('')
    for i in range(board_size):
        down = ''
        for x in range(board_size - 1):
            down += '     |'
        cross = ''
        for x in range(board_size):
            if x < board_size - 1:
                cross += '_____|'
            else:
                cross += '_____'
        selection_values = board[i][:board_size]
        selection_format = ''
        for value in selection_values:
            if len(str(value)) == 1:
                selection_format += '  {}  |'
            elif len(str(value)) == 2:
                selection_format += ' {}  |'
            elif len(str(value)) == 3:
                selection_format += ' {} |'
            else:
                selection_format += '{} |'
        selection_format = selection_format[:-1]
        selection = selection_format.format(*selection_values)
        print(down)
        print(selection)
        if i == board_size - 1:
            print(down)
        else:
            print(cross)