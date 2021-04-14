i=10

while i>0:
 print("Press 1: add")
 print("Press 2: substract")
 print("Press 3: multiply")
 print("Press 4: division")
 print("Press 0: Exit")
 s = int(input("Enter your prefered operation: "))
 
 if s==1:
  a = int(input("Enter first no: "))
  b = int(input("Enter 2nd no: "))
  print("Result: ",a+b,"\n")
  i-=1
 elif s==2:
  a = int(input("Enter first no: "))
  b = int(input("Enter 2nd no: "))
  print("Result: ",a-b,"\n")
  i-=1
 elif s==3:
  a = int(input("Enter first no: "))
  b = int(input("Enter 2nd no: "))
  print("Result: ",a*b,"\n")
  i-=1
 elif s==4:
  a = int(input("Enter first no: "))
  b = int(input("Enter 2nd no: "))
  print("Result: ",a/b,"\n")
  i-=1
 elif s==0:
  print("\nThank you for using.")
  break
 else:
  print("\nInvalid operation selection")
  i-=1
