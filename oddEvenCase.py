def alt_case(s):
    new = []
    print(s)
    for x in range(len(s)):
        if x%2==0:
            new.append(s[x].upper())
        else:
            new.append(s[x].lower()) 
    return ''.join(new)

print(alt_case('supercalifragilisticexpialidocious'))