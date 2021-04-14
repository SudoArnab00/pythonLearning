s = int(input("1: Celsius to Fahrenheit \n2: Fahrenheit to Celsius\nEnter choice: "))
if s==1:
    c=float(input("Enter temp. in celsius: "))
    print("Fahrenheit: ",(c*9/5)+32)
elif s==2:
    c=float(input("Enter temp. in fehrenheit: "))
    print("Celsius: ",(c-32)*0.5556)
else:
    print("Wrong input")
