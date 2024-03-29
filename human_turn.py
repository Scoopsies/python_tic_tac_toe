from print_board import print_board
from computer_turn import available_moves

class OccupiedSpaceError(Exception):
    pass

def human_turn(board) -> list[list[str]]:
    player_choice = input(f'Please select a spot. (1 - {len(board) ** 2})\n \n')
    available = available_moves(board)
    updated_board = update_board(board, player_choice, available)
    return updated_board

def update_board(board, player_choice, available):
    error = False
    while True:
        try:
            if error:
                player_choice = input(f'Please select a spot. (1 - {len(board) ** 2})\n \n')
            choice_index = int(player_choice) - 1
            if not (int(player_choice) in available):
                raise OccupiedSpaceError()
            y_axis = int((choice_index)/ len(board))
            x_axis = choice_index % len(board)
            board[y_axis][x_axis] = 'X'
            return board
        except ValueError:
            print_board(board)
            print(f'\n{player_choice} is not a valid input.')
            error = True
        except IndexError:
            print_board(board)
            print(f'\n{player_choice} is not in range 1 - {len(board) ** 2}.')
            error = True
        except OccupiedSpaceError:
            print_board(board)
            print(f'\n{player_choice} has already been chosen.')
            error = True