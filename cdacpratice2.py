"""
Write a Python program that takes a number from the user and classifies it as positive, negative, or zero. 
Use if-elif-else statements to implement this.
"""


a=int(input("Enter a number: "))

if(a>0):
    print("The number is positive")
elif(a<0):
    print("The number is negative")
elif(a==0):
    print("The number is zero")