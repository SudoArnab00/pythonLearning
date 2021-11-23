import random

words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']
word = random.choice(words)

turn = 12
guesses = ''

while turn>0:
	flag = 0
	for chars in word:
		if chars in guesses:
			print(chars,end='')
		else:
			print("_ ",end='')
			flag+=1
	
	if flag == 0:
		print('\nGreat job! The word was',word)
		break	
	
	guess = input("\nYour guess? ")
	print('\n')
	guesses+=guess

	if guess not in word:
		turn-=1
		print('Wrong! You have ',turn,' turns left')
		if turn == 0:
			print('\nYou lost! The word was ',word)
			break