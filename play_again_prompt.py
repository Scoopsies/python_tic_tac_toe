def play_again_prompt() -> bool:
    while True:
        player_response = input('Would you like to play again? Y/N \n').lower()
        if player_response == 'n':
            return True
        elif player_response == 'y':
            return False
        else:
            print('\nInvalid Response.')