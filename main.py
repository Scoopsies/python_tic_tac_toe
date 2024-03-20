from print_board import print_board
from win_checker import win_checker

def new_game():
    board = [
        ['1','2','3'], 
        ['4','5','6'],
        ['7','8','9']
    ]
    win = False
    turn = 0
    
    while win == False and turn < 9:
        print_board(board)

        while True:
            try:
                player_choice = input('Where do you want to play? \n \n')
                choice_index = int(player_choice) - 1
                if 0 <= choice_index <= 8:
                    break
                else:
                    raise ValueError()
                    # print_board(board)
                    # print(f'"{player_choice}" is not a valid input. Please choose a number between 1 and 9.')
            except:
                print_board(board)
                print(f'{player_choice} is not a valid input. Please choose a number between 1 and 9.')

        y_axis = int((choice_index)/ 3)
        x_axis = choice_index % 3
        board[y_axis][x_axis] = 'X'
        win = win_checker(board)
        turn += 1

    print_board(board)
    print('You Win!')

new_game()