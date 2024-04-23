from board_type import Board

def available_moves(board : Board):
    result = []
    for list in board:
        for value in list:
            if value != 'X' and value != 'O':
                result.append(int(value))
    return result