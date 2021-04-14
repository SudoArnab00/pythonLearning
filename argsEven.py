def myfunc(*args):
    even = []
    for x in args:
        if x%2==0:
            even.append(x)
        else: pass
    return even

print(myfunc(2,4,1,5,8))