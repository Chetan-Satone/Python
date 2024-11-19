"""Write a Python program that takes two integers from the user and checks if the first number is divisible by the second number.
The program should use a conditional if-else statement to print whether the first number is divisible by the second or not."""


a=int(input("Enter any number"))
b=int(input("Enter any number"))

if(a%b==0):
    print("The number is divisible by b")
else:
    print("The number is not divisible.")