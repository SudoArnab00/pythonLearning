from random import shuffle
def shuffle_list(mylist):   #Preparing the list to play
    shuffle(mylist)
    return mylist

def player_guess(): #Taking Guess from user
    guess = ''
    while guess not in ['0','1','2','3']:
        guess = input("Pick a number 0, 1, 2 or 3: ")
    return int(guess)

def check(playlist,guess):  #Win/lose Checking
    if playlist[guess] == 'O':
        print("Congrats, you found the ball")
    else:
        print("OOPS!!")
        print(playlist)

'''
def game_begin():
    thelist = [' ',' ','O',' ']
    mixed_list = shuffle_list(thelist)      #Mixed the list up
    guess = player_guess()
    check(mixed_list,guess)

print(game_begin())'''

thelist = [' ',' ','O',' ']
mixed_list = shuffle_list(thelist)      #Mixed the list up
guess = player_guess()
check(mixed_list,guess)