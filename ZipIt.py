mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
#returns till the shortest list ad discards the rest of extra items in list1

for item in zip(mylist1,mylist2,mylist3):
    print(item)