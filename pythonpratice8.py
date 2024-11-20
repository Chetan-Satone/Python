"""Palindrome Checker

Write a Python program that checks if a given string is a palindrome (i.e., it reads the same forward and backward). 
The program should ignore spaces, punctuation, and case sensitivity when performing the check.
"""

def palindrome(string):
    if(string==string[::-1]):
        return"The string is palidrome"
    else:
        return"The string is not palidrome"
    
string=input("enter a string:")
print(palindrome(string))
