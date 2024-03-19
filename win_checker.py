def win_checker(board):
    for i in range(3):
        row = []
        column = []
        diagonal_forward = []
        diagonal_backward = []
        backward_count = 2
        win_x = ['X','X','X']
        win_o = ['O', 'O', 'O']
        for x in range(3):
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