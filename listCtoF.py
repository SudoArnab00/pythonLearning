celcius = [0,20,30,40]
fah = [((9/5)*temp + 32) for temp in celcius]
print(celcius, " to ", fah)

# OR

#fah = []
#for temp in celcius:
#    fah.append((9/5)*temp + 32)
#print(fah)