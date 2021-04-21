# Euclid's algorithm for GCD

def EUalgo(x,y):
    if y > x:
        t = x
        x = y
        y = t
    elif x % y == 0 or x == y:
        return y
    else:
        while 1:
            z = round(x / y)
            m = x - (z * y)

            if x%y != 0:
                gcd = y

            if m==0:
                break
            
            x = y
            y = m
            gcd = m

        return gcd

print(EUalgo(1980, 1617))