# reverse a integer string (user input)
c = input("string: ")
t=0
count=0
n=c

for i in c:
 count+=1

c = int(c)
for i in range(count):
 r=c%10
 t=(t*10)+r
 c=c//10

print(n," when reversed is",t)
