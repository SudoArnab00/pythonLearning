def countit(user):
    count = {}  # empty dictionery
    for i in user:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

count_user_input = input("Enter a word: ")
print(countit(count_user_input))