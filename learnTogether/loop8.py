#Sum of digits of a number (user input)
n = input("enter number: ")
add_it=0
for i in range(len(n)):
 digi = int(n[i])
 add_it = add_it + digi
print(add_it)
