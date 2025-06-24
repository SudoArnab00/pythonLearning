# Generate Fibonacci series up to N terms (user input)
n = int(input("Enter length of fibonacci: "))

a=0
b=1

print(a,end=' ')
print(b,end=' ')

for i in range(1,n):
 c=a+b
 a=b
 b=c
 print(c,end=' ')

print("\n")
