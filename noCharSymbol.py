n = input("Enter a character: ")
chk = ord(n)

if chk>64 and chk<91 or chk>96 and chk<123:
    print("It is an alphabet")
elif chk>47 and chk<58:
    print("It is a number")
else:
    print("It is a special symbol")
