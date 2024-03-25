def print_board(board):
    for i in range(3):
        down = '     |     |'
        cross = '_____|_____|_____'
        selection = '  {}  |  {}  |  {}'.format(board[i][0],board[i][1],board[i][2])
        print(down)
        print(selection)
        if i == 2:
            print(down)
        else:     
            print(cross)