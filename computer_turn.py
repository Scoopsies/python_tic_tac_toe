from win_checker import win_checker

def computer_turn(board: list[list[str]]):
    move_choices = available_moves(board)
    choice_index = move_choices[0] - 1
    y_axis = int((choice_index)/ len(board))
    x_axis = choice_index % len(board)
    board[y_axis][x_axis] = 'O'
    return board

def miniMax(board: list[list[str]]):
    move_choices = available_moves(board)
    print(type(move_choices[0]))
    turn = len(board) ** 2 - len(move_choices)
    print(move_choices)

def available_moves(board : list[list[str]]):
    result = []
    for list in board:
        for value in list:
            if value != 'X' and value != 'O':
                result.append(int(value))
    return result

