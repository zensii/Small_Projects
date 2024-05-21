import random

options = ['[R]ock', '[P]aper', '[S]cissor']

player = input('Player Name: ')

while True:
    print()
    player_pick = input(f'{player} choose your weapon:{options}: ').capitalize()

    if player_pick == 'End':
        break
    elif player_pick not in options:
        print(f'{player_pick} is not a valid option')
        continue

    computer_pick = random.choice(options)
    print(f'Computer choose {computer_pick}')
    print()

    if player_pick == computer_pick:
        print(f'{player} and The Computer are a tie')
        continue

    elif player_pick == 'Rock':
        if computer_pick == 'paper':
            print(f'{computer_pick} beats {player_pick}, The Computer wins')
            continue
        else:
            print(f'{player_pick} beats {computer_pick}, {player} wins')
            continue

    elif player_pick == 'Scissor':
        if computer_pick == 'Rock':
            print(f'{computer_pick} beats {player_pick}, The Computer wins')
            continue
        else:
            print(f'{player_pick} beats {computer_pick}, {player} wins')
        continue
    elif player_pick == 'Paper':
        if computer_pick == 'Scissor':
            print(f'{computer_pick} beats {player_pick}, The Computer wins')
            continue
        else:
            print(f'{player_pick} beats {computer_pick}, {player} wins')
            continue


