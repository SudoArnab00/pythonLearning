nos = input("Enter a number: ")
n = int(nos)
sum=0
dig=0
for i in nos:
    r = n%10
    sum = sum + r
    dig = (dig*10) + r
    n = (n-r)/10

print("Digit sum: ",sum)

if int(dig) == int(nos):
    print("Palindrome")
else:
    print("Not Palindrome")
