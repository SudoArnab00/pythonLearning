# if letters in a word is rearranged and a meaning word is formed then they are anagrams
def anagram_check(wrd1, wrd2):
    wrd1 = wrd1.lower()
    wrd2 = wrd2.lower()
    return sorted(wrd1) == sorted(wrd2)

print(anagram_check("CiNema","IcemAn"))
print(anagram_check("Man","WomaN"))
print(anagram_check("LoCo","Cool"))