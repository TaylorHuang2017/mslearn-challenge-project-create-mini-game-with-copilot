# write a simple game in which each player chooses one of the three options: rock, paper, or scissors.
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random
import sys

def game():
    player_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input('Choose rock, paper or scissors: ')
        player_choice = player_choice.lower()
        if player_choice not in options:
            print('Invalid option, please choose rock, paper or scissors.')
            continue
        computer_choice = random.choice(options)
        print(f'Computer choice: {computer_choice}')
        if player_choice == computer_choice:
            print('It\'s a tie!')
        elif player_choice == 'rock':
            if computer_choice == 'paper':
                print('Computer wins!')
                computer_score += 1
            else:
                print('Player wins!')
                player_score += 1
        elif player_choice == 'paper':
            if computer_choice == 'scissors':
                print('Computer wins!')
                computer_score += 1
            else:
                print('Player wins!')
                player_score += 1
        elif player_choice == 'scissors':
            if computer_choice == 'rock':
                print('Computer wins!')
                computer_score += 1
            else:
                print('Player wins!')
                player_score += 1
        print(f'Player score: {player_score}')
        print(f'Computer score: {computer_score}')
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break
    print('Game over!')
    print(f'Player final score: {player_score}')
    print(f'Computer final score: {computer_score}')

if __name__ == '__main__':
    game()
    sys.exit()  
