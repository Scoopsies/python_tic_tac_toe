def win_checker(board) -> bool:
    board_length = len(board)
    for i in range(board_length):
        row = []
        column = []
        diagonal_forward = []
        diagonal_backward = []
        backward_count = board_length - 1
        win_x = []
        for x in range(board_length):
            win_x.append('X')
        win_o = []
        for x in range(board_length):
            win_o.append('O')
        for x in range(board_length):
            row.append(board[i][x])
            column.append(board[x][i])
            diagonal_forward.append(board[x][x])
            diagonal_backward.append(board[x][backward_count])
            backward_count -= 1

        if row == win_x or row == win_o:
            return True
        elif column == win_x or column == win_o:
            return True
        elif diagonal_forward == win_x or diagonal_forward == win_o:
            return True
        elif diagonal_backward == win_x or diagonal_forward == win_o:
            return True
    
    return False