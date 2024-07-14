from colorama import Fore, Style, init
import copy
init()

game_name = """
 #######             #######                  #######               
    #    #  ####        #      ##    ####        #     ####  ###### 
    #    # #    #       #     #  #  #    #       #    #    # #      
    #    # #            #    #    # #            #    #    # #####  
    #    # #            #    ###### #            #    #    # #      
    #    # #    #       #    #    # #    #       #    #    # #      
    #    #  ####        #    #    #  ####        #     ####  ######                                                            
"""


def display_board(board):
    for row in board:
        print(''.join(row))


empty_board = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]
position_board = [['[7]', '[8]', '[9]'], ['[4]', '[5]', '[6]'], ['[1]', '[2]', '[3]']]


def player_input(first_choice, second_choice):
    player_marker = None
    while player_marker is None:
        player_input = input(f"Choose '{first_choice}' or '{second_choice}': ").upper()
        if player_input == first_choice or player_input == second_choice:
            player_marker = player_input
        else:
            print(Fore.RED + f'Please type {first_choice} or {second_choice}' + Style.RESET_ALL)
    return player_marker


def place_marker(board, position, marker):
    if position == 1:
        board[2][0] = '[' + marker + ']'
    elif position == 2:
        board[2][1] = '[' + marker + ']'
    elif position == 3:
        board[2][2] = '[' + marker + ']'
    elif position == 4:
        board[1][0] = '[' + marker + ']'
    elif position == 5:
        board[1][1] = '[' + marker + ']'
    elif position == 6:
        board[1][2] = '[' + marker + ']'
    elif position == 7:
        board[0][0] = '[' + marker + ']'
    elif position == 8:
        board[0][1] = '[' + marker + ']'
    elif position == 9:
        board[0][2] = '[' + marker + ']'

    return board


def win_check(board, mark):
    # check rows
    checker = '[' + mark + ']'
    for row in board:
        if all(pos == checker for pos in row):
            return True
    # check columns
    for row in range(3):
        counter = 0
        for column in range(3):
            if board[column][row] == checker:
                counter += 1
                if counter == 3:
                    return True
    # check first diagonal
    if board[0][0] == board[1][1] == board[2][2] == checker:
        return True
    # check other diagonal
    if board[2][0] == board[1][1] == board[0][2] == checker:
        return True

    return False


import random


def choose_first(first_player, second_player):
    players = [first_player, second_player]
    first_plays = random.choice(players)
    if first_plays == first_player:
        return first_player
    return second_player


def space_check(board, position):
    if position == 1:
        if board[2][0] == '[ ]':
            return True
    elif position == 2:
        if board[2][1] == '[ ]':
            return True
    elif position == 3:
        if board[2][2] == '[ ]':
            return True
    elif position == 4:
        if board[1][0] == '[ ]':
            return True
    elif position == 5:
        if board[1][1] == '[ ]':
            return True
    elif position == 6:
        if board[1][2] == '[ ]':
            return True
    elif position == 7:
        if board[0][0] == '[ ]':
            return True
    elif position == 8:
        if board[0][1] == '[ ]':
            return True
    elif position == 9:
        if board[0][2] == '[ ]':
            return True
    return False


def full_board_check(board):
    for row in board:
        for cell in row:
            if cell == '[ ]':
                return False
    return True


def player_choice(board):
    next_position = None
    while next_position == None:
        print(Style.RESET_ALL)
        usr_input = input('Please enter the next position(1-9): ')
        if usr_input.isdigit():
            if 1 <= int(usr_input) <= 9:
                next_position = int(usr_input)
                if space_check(board, next_position):

                    return next_position
                else:
                    print(Fore.RED + 'Position already taken!')
                    print()
                    next_position = None

            else:
                print(Fore.RED + 'Number not in range 1-9!')
                print()
        else:
            print(Fore.RED + 'Input not a number in range 1-9!')
            print()


def replay():
    again = player_input('Y', 'N')
    if again.upper() == 'Y':
        print('\n' * 100)
        return True
    return False


print()
print('Welcome to:')
print(game_name)


while True:
    # first player selects marker
    first_player_marker = player_input('X', 'O')
    if first_player_marker == 'X':
        second_player_marker = 'O'
    else:
        second_player_marker = 'X'

    # game begins.Resets and shows empty board
    print()
    print("Lets's play!")
    print()
    print('To enter your move enter the required position based on this mapping: ')
    for row in position_board:
        print(''.join(row))
    print()

    # game selects who plays first
    mark = choose_first(first_player_marker, second_player_marker)
    print()
    print(f'Player {mark} will play first.')
    print()
    board = copy.deepcopy(empty_board)
    display_board(board)
    print()
    # players start playing and alternating moves
    is_draw = False
    while not full_board_check(board):

        print(f"It's player {mark}'s turn.")
        next_position = player_choice(board)
        board = place_marker(board, next_position, mark)
        # check for win
        if win_check(board, mark):
            winning_board = copy.deepcopy(board)
            colored_mark = Fore.GREEN + mark + Style.RESET_ALL
            for i, row in enumerate(winning_board):
                for j, pos in enumerate(row):
                    if pos == '[' + mark + ']':
                        winning_board[i][j] = '[' + colored_mark + ']'
            print('\n' * 100)
            display_board(winning_board)
            print(Style.RESET_ALL)
            print()
            print(Fore.GREEN + f"Player {mark} wins the round!")
            print(Style.RESET_ALL)
            print()
            break

        # continue next turn
        print('\n' * 100)
        display_board(board)

        # select next player
        if mark == second_player_marker:
            mark = first_player_marker
        else:
            mark = second_player_marker
        print()
    else:
        print("It's a DRAW!")

    print()
    print('Do you want to play another round? ')
    if not replay():
        print('Bye, bye...')
        break