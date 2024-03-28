def win_checker(board, turn) -> bool:
    if (turn % 2):
        x_or_o = 'O'
    else: 
        x_or_o = 'X'
    board_length = len(board)
    for i in range(board_length):
        row = []
        column = []
        diagonal_forward = []
        diagonal_backward = []
        backward_count = board_length - 1
        win_conditions = []
        for x in range(board_length):
            win_conditions.append(x_or_o)
        # win_o = []
        # for x in range(board_length):
        #     win_o.append('O')
        for x in range(board_length):
            row.append(board[i][x])
            column.append(board[x][i])
            diagonal_forward.append(board[x][x])
            diagonal_backward.append(board[x][backward_count])
            backward_count -= 1

        if row == win_conditions:
            return True
        elif column == win_conditions:
            return True
        elif diagonal_forward == win_conditions:
            return True
        elif diagonal_backward == win_conditions:
            return True
    
    return False