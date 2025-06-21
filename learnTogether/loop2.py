#Sum of numbers from 1 to N (user input)
N=int(input("Sum till N - "))
sum=0
for i in range(1,N+1):
 sum=sum+i
 print(i,end=' ')
print("\nSummation :",sum)
