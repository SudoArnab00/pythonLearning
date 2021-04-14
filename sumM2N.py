m = int(input("Enter start: "))
n = int(input("Enter end: "))
add=0
i=m
while i>0:
    add=add + i;
    i-=1
print(1," to ",m," adds up to ",add)

add=0
i=m
while i<=n:
    add=add + i;
    i+=1
print(m," to ",n," adds up to ",add)
    
