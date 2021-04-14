def searchit(list_,s):
    for i in list_:
        if i == s:
            break
    return True


a = int(input("Enter a start: "))
b = int(input("Enter a end: "))

elements = range(a,b)  # creating random list

item = int(input("What to search? "))   # asking for search item
print(searchit(elements,item))