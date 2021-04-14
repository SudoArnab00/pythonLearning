import math
s = int(input("1: Sphere Area & Volume \n2: Cone Area & Volume \nEnter choice: "))
if s==1:
    r=float(input("Enter radius of sphere: "))
    print("Area: ",4*3.142*r*r)
    print("Volume: ",(4*3.142*r*r*r)/3)
elif s==2:
    r=float(input("Enter radius of cone: "))
    h=float(input("Enter height of cone: "))
    print("Area: ",3.142*r*(r+math.sqrt((h*h)+(r*r))))
    print("Volume: ",(3.142*r*r*h)/3)
else:
    print("Wrong input")