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

            while True:
                player_choice = input('Where do you want to play? \n \n')
                try:
                    choice_index = int(player_choice) - 1
                    y_axis = int((choice_index)/ 3)
                    x_axis = choice_index % 3
                    if 0 <= choice_index <= 8 and board[y_axis][x_axis] != 'X':
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print_board(board)
                    print(f'{player_choice} is not a valid input. Please choose a number between 1 and 9.')

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
