def listEvenCheck(mylist = []):
    myEven = []
    for n in mylist:
       if n%2==0:
           myEven.append(n)
       else: pass
    return myEven

print(listEvenCheck([21,41,13,4,82,91]))