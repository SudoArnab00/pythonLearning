#Count the number of vowels in a string (user input)
c=input("enter string: ")
vowel=0
lower_c=c.lower()
for i in range(len(c)):
 if(lower_c[i] == 'a' or lower_c[i] == 'e' or lower_c[i] == 'i' or lower_c[i] =='o' or lower_c[i] == 'u'):
  vowel+=1
print("Number of vowels: ",vowel)
