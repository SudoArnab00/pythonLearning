import random

characters = "qwertasgdfzvxbcnhyjnuimkl,op;,'.[]/1238765490-=+!&@^#&*$)%*<>?:{}"
pswrd=''
length = int(input("How long do you want the password to be? "))
for i in range(length):
    pswrd += random.choice(characters)

print(pswrd)