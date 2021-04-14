s = int(input("1: KM to M \n2: M to CM \n3: Mins to Seconds\nEnter choice: "))
if s==1:
    d=float(input("Enter distance in KM: "))
    print("It will be: ",d*1000," metres")
elif s==2:
    l=int(input("Enter length in metres: "))
    print("It will be: ",l*100," centimetres")
elif s==3:
     t=int(input("Enter time in minutes: "))
     print("It will be: ",t*60," Seconds")
else:
    print("Wrong input")
