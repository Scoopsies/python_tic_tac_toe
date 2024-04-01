from custom_types import Board

def win_checker(board: Board, turn: int) -> str:
    if not (turn % 2):
        x_or_o = 'X'
    else: 
        x_or_o = 'O'

    board_length = len(board)
    for i in range(board_length):
        win_conditions = []
        for x in range(board_length):
            win_conditions.append(x_or_o)

        row = []
        column = []
        diagonal_forward = []
        diagonal_backward = []
        backward_count = board_length - 1
        for x in range(board_length):
            row.append(board[i][x])
            column.append(board[x][i])
            diagonal_forward.append(board[x][x])
            diagonal_backward.append(board[x][backward_count])
            backward_count -= 1

        if row == win_conditions:
            if x_or_o == 'X':
                return 'You Win!'
            else:
                return 'You Lose.'
        elif column == win_conditions:
            if x_or_o == 'X':
                return 'You Win!'
            else:
                return 'You lose.'
        elif diagonal_forward == win_conditions:
            if x_or_o == 'X':
                return 'You Win!'
            else:
                return 'You Lose.'
        elif diagonal_backward == win_conditions:
            if x_or_o == 'X':
                return 'You Win!'
            else:
                return 'You Lose.'
                
    return 'no winner'

