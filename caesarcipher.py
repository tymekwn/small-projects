import string
letterlist = list(string.ascii_lowercase)
word = list(input("Input a word").lower())
newword=[]
change = int(input("Change?"))
if change <0:change+=26
digits = {num:letterlist[num] for num in range(26)}
newdigits = {num:letterlist[num-(26-change)]for num in range(26)}

for i in range(len(word)):
    if word[i] in digits.values():
        newletter = list(digits.keys())[list(digits.values()).index(word[i])]
        newword.append(newdigits[newletter])
    else:newword.append(word[i])
    
print("".join(newword))
        
               
