"""Write a program that checks if a given year is a leap year or not. A leap year occurs if:

    The year is divisible by 4
    If divisible by 100, it must also be divisible by 400."""

i = int(input("Enter the year: "))

if(i % 4 == 0 and i % 100 !=0) or (i % 400 ==0):
    print("Yeah, It is leap year bro.")
else:
    print("It is not a leap year dude.")