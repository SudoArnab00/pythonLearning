mylist1 = [x for x in range(0,51,3)]
print(mylist1)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word + ' is Even')