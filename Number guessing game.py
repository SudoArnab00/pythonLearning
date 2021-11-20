import random

start = int(input("Enter Lower limit "))
end = int(input("Enter upper limit "))
tries = random.randint(4,10)
star = random.randint(start,end)
guesses = 1
print("\t~~You get ",tries," guesses~~")

for i in range(start,end):
    user_guess = int(input("Guess the number: "))
    if guesses < tries:
        if user_guess > star:
            print("Too High")
            guesses+=1 
        elif user_guess < star:
            print("Too Low")
            guesses+=1 
        elif user_guess == star:
            print("You are correct! You took ",guesses," guesses")
            break
    else:
        print("Sorry, no more guesses left. \n The Number is ",star)