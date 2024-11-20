"""Find Substring Occurrences

Write a Python program that takes two strings as input: a main string and a substring. 
The program should count how many times the substring appears in the main string, without overlapping.

"""


"""everse Words in a String

Write a Python program that takes a sentence as input and reverses the order of the words in the sentence, 
but keeps the characters in each word in their original order."""


string=str(input("enter any sentence"))

s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
    print(" ".join(l))