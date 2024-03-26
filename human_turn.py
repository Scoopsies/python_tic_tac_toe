from print_board import print_board

def human_turn(board) -> list[list[str]]:
    print_board(board)
    board_length = len(board)
    player_choice = input(f'Where do you want to play? (1 - {board_length ** 2})\n \n')

    while True:
        try:
            choice_index = int(player_choice) - 1
            y_axis = int((choice_index)/ board_length)
            x_axis = choice_index % board_length

            if not (0 <= choice_index <= board_length ** 2 - 1):
                raise IndexError()
            if board[y_axis][x_axis] == 'X' or board[y_axis][x_axis] == 'O':
                raise ValueError()
            break
        except ValueError:
            print_board(board)
            player_choice = input(f'{player_choice} has already been chosen. Please select an unchosen spot. (1 - {board_length ** 2}) \n \n')
        except IndexError:
            player_choice = input(f'{player_choice} is not in range 1-9. Please select an unchosen spot. (1 - {board_length ** 2}) \n\n')

    board[y_axis][x_axis] = 'X'
    return board
