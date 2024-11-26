per = int(input("enter the percentage"))

if per>=90:
    grade = "A"
elif per>=80 and per<90:
    grade = "B"
elif per>=60 and per<80:
    grade = "C"
        
elif per>=40 and per<60:
    grade = "D"  
else:
    grade = "F"
    
print(f" per = {per} grade = { grade}")