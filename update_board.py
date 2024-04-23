from print_board import print_board
from board_type import Board

class OccupiedSpaceError(Exception):
    pass

def update_board(board: Board, player_choice: str, available_moves: list[int]) -> Board:
    error = False
    turn = (len(board) ** 2 - len(available_moves))
    while True:
        try:
            if error:
                player_choice = input(f'Please select a spot. (1 - {len(board) ** 2})\n \n')
            choice_index = int(player_choice) - 1
            if not (int(player_choice) in available_moves):
                raise OccupiedSpaceError()
            y_axis = int((choice_index)/ len(board))
            x_axis = choice_index % len(board)

            if (turn % 2): 
                board[y_axis][x_axis] = 'O'
            else:
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