# count space, number and charactera in a string
c="python is 15 times better"
space=0
ch=0
num=0

for i in c:
 if ord(i)==32:
  space=space+1
 
 elif ord(i)>=48 and ord(i)<=57:
  num=num+1

 elif ord(i.lower())>=97 and ord(i.lower())<=122:
  ch=ch+1

print("Space:",space)
print("Numbers:",num)
print("Characters:",ch)
