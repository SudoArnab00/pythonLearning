import random
turns = 3
cpu_win = 0
user_win = 0
while turns > 0:
    # user choice
    print('1: Rock\n2: Paper\n3: Scissor')
    user_choice = int(input("Choose: "))
    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    elif user_choice == 3:
        user_choice_name = "Scissor"
    
    # cpu choice
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        cpu_choice_name = "Rock"
    elif cpu_choice == 2:
        cpu_choice_name = "Paper"
    elif cpu_choice == 3:
        cpu_choice_name = "Scissor"
    
    turns -= 1
    print(cpu_choice_name," VS ", user_choice_name)

    # choice checking
    if (cpu_choice == 1 and user_choice == 3) or (cpu_choice == 2  and user_choice == 1) or (cpu_choice == 3 and user_choice == 2):
        print(cpu_choice_name," Wins \n")
        print('Sorry, You lose\n')
        cpu_win += 1
    
    elif (user_choice == 1 and cpu_choice == 3) or (user_choice == 2  and cpu_choice == 1) or (user_choice == 3 and cpu_choice == 2):
        print('\nCongratulations')
        print(cpu_choice_name," Wins ")
        user_win += 1
    
    else:
        print('Tied\n')

if cpu_win > user_win:
    print("\n~~CPU Wins~~\n")
elif user_win > cpu_win:
    print("\n~~You Win~~\n")
else:
    print("\n~~Match TIED~~\n")