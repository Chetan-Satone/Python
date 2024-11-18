#for next line add \n
#
#concatenation   in this we can add string by print(str1 + str2)                                    
# 

#str = "Triumph" 
#print(str[1:len(str)])     #slicing

#print(str[-3:-1])          #negative also from right to left

"""str = "I am$ decoder$"

print(str.endswith("er"))

print(str.capitalize())

print(str.replace("am","you"))

print(str.find("m"))

print(str.count("d"))


print(str.count("$"))"""


"""str = int(input("Enter your age: "))

if(str<=18):
    print("your age is not valid")

elif(str>=18):
    print("Your are valid for license")"""

a = int(input("Enter the no.A: "))
b = int(input("Enter no.B: "))
c = int(input("Enter no.C: "))
d = int(input("Enter no.D: "))

if(a>b and a>c and a>d):
    print("The number A is greater")
elif(b>a and b>c and b>d):
    print(" The number B is greater.")
elif(c>a and c>b and c>d):
    print("The number C is greater.")    
elif(d>a and d>b and d>c):
    print("The no.D is greater.")