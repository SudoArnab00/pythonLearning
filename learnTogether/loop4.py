#Print multiplication table of a number (user input)
N=int(input("enter Number: "))
multi=1
for i in range(1,11):
 multi = N * i
 print(N," x ",i,"=",multi,"\n")

