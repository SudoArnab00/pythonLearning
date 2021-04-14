'''v = input("Enter a character: ")
vowel = ["a", "e", "i", "o", "u"]
for i in vowel:
    if v == vowel[i]:          
        print("Vowel")
        break

    else:
        print("Consonent")'''

v = input("Enter a character: ")
vowel = ["a", "e", "i", "o", "u"]
if v=='a' or v=="e" or v=="i" or v=="o" or v=="u":
    print("Vowel")
else:
    print("Consonent")
