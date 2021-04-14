def spy(mynum):
    numList = [0,0,7,'x']
    for i in mynum:
        if i == numList[0]:
            numList.pop(0)
        else: pass
    return len(numList)==1

print(spy([1,2,4,0,7,5,0,2]))