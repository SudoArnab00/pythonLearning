#Find the factorial of a number (user input)
n=int(input("enter number: "))
fact = 1
for i in range(1,n+1):
 fact = fact * i
print("factorial:",fact)
