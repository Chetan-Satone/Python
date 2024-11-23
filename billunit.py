unit = int(input("enter the unit"))

if unit<100:
    amt = unit*1
elif unit<300:
    amt = 100 + (unit-100)*2
elif unit>300:
    amt = 100 + (200*2) + (unit-300)*3

print(amt)