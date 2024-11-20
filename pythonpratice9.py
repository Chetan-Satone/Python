"""Count Vowels and Consonants

Create a Python program that takes a string as input and counts the number of vowels and consonants in it. 
Ignore spaces and punctuation. Your program should output the count of vowels and consonants separately.
"""



vcount=0
ccount=0
str= "This is sentence for demo."

str=str.lower()

for i in range(0,len(str)):
    if str[i] in ("a", "e", "i","o", "u"):
        vcount= vcount + 1
    elif(str[i]>='a' and str[i]<='z'):
        ccount= ccount + 1
        print("The total number of vowels and consonant are")
        print(vcount)
        print(ccount)