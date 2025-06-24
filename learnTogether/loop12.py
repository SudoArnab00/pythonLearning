# remove vowel from string

n="I am AwEsome"
checker='aeiouAEIOU'
noVowel=''

for i in n:
 if i not in checker:
  if ord(i)!=32:
   noVowel=noVowel+i

print(noVowel)
