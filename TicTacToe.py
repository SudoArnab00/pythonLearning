# prepare the board
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# mark the user
def player_input():
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input('Player 1: x or o? ')
    p1 = marker
    if p1 == 'x':
        p2 = 'o'
    else: p2 = 'x'

    return (p1,p2)

# Placing the markers
def place_inputs(board, position, marker):
    board[position] = marker


# Check the wins
def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[7]==board[8]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or
    (board[7]==board[5]==board[3]==mark) or
    (board[7]==board[4]==board[1]==mark) or
    (board[8]==board[5]==board[2]==mark) or
    (board[9]==board[6]==board[3]==mark))

# Randomizing the player
import random
def choose_player():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Check which moves are left
def move_left(board, position):
    return board[position] == ' '

# Check to see board is full or not
def full_board_check(board):
    for i in range(1,10):
        if move_left(board,i):  # If moves are left then there is space and board not full
            return False
    # board is full if we return True
    return True

# Check if move is possible
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not move_left(board,position):
        pos = int(input('Choose your move: (1-9) '))
    return pos

# Replay the game?
def replay():
    choice = input('Want to play again? Enter Y or N ')
    return 'Y'

###########################################

# Lets Play the game
print('Welcome to Tic Tac Toe!! ')

while True:
    # Set everything up
    the_board = [' ']*10    #list of 10 empty strings
    p1marker,p2marker = player_input()
    
    turn = choose_player()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')
    if play_game == 'y':
        game_on = True
    else: game_on = False

    # Game play
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)    #display board
            position = player_choice(the_board)     # choose a position
            place_inputs(the_board,p1marker,position)   # place the marker in position
            # Check if they won
            if win_check(the_board,p1marker):
                display_board(the_board)
                print("Player 1 won!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            #display board
            display_board(the_board)
            # choose a position  
            position = player_choice(the_board)     
            place_inputs(the_board,p2marker,position)   # place the marker in position
            # Check if they won
            if win_check(the_board,p2marker):
                display_board(the_board)
                print("Player 2 won!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break