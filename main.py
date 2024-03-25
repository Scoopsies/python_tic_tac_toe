from print_board import print_board
from win_checker import win_checker

def new_game():
    while True:
        board = [
            [1,2,3], 
            [4,5,6],
            [7,8,9]
        ]

        win = False
        turn = 0
        player_turn = True
        
        while win == False and turn < 9:
            print_board(board)
            player_choice = input('Where do you want to play? (1 - 9)\n \n')

            while True:
                try:
                    choice_index = int(player_choice) - 1
                    y_axis = int((choice_index)/ 3)
                    x_axis = choice_index % 3

                    if not (0 <= choice_index <= 8):
                        raise IndexError()
                    if board[y_axis][x_axis] == 'X' or board[y_axis][x_axis] == 'O':
                        raise ValueError()
                    break
                except ValueError:
                    print_board(board)
                    player_choice = input(f'{player_choice} has already been chosen. Please select an unchosen spot. (1 - 9) \n \n')
                except IndexError:
                    player_choice = input(f'{player_choice} is not in range 1-9. Please select an unchosen spot. (1-9)')


            y_axis = int((choice_index)/ 3)
            x_axis = choice_index % 3
            board[y_axis][x_axis] = 'X'
            win = win_checker(board)
            turn += 1

        print_board(board)
        print('You Win!')
        if ('n' == input('Would you like to play again? Y/N \n').lower()):
            break

new_game()
