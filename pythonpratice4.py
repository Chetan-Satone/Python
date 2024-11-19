"""Write a program that prints numbers from 1 to 100, but:

    For numbers that are divisible by 3, print "Fizz" instead of the number.
    For numbers that are divisible by 5, print "Buzz" instead of the number.
    For numbers divisible by both 3 and 5, print "FizzBuzz".
"""

for i in range(0,101):
    if(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    elif(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    else:
        print(i)