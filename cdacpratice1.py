id= int(input("Enter the roll number:"))
prm= int(input("enter your  pratical marks"))
inm= int(input("enter your internal marks"))
ccem= int(input("enter your cce marks"))

total=prm+inm+ccem

if(total > 60):
    print("passed")
else:
    print("failed")