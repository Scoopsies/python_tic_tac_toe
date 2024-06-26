from board_type import Board

def create_board() -> Board:
    board_size = input('How big of a board would you like? (3 - 15) \n\n')
    # Checks if input is valid integer 3 - 15 before creating the board.
    while True:
        try:
            if  not (3 <= int(board_size) <= 20):
                raise ValueError()
            board_size = int(board_size)
            break
        except ValueError:
            board_size = input(f'\n{board_size} is not a valid option. Pick a number 3 - 15. \n\n')


    counter = 1
    board = []
    for i in range(board_size):
        row = []
        for x in range(board_size):
            row.append(str(counter))
            counter += 1
        board.append(row)
    return board