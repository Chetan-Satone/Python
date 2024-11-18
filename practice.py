"""n=int(input(print("Type any number: ")))

if(n%2!=0):
    print("Weird")
elif(n>=2 and n<=5):
    print("Not Weird")
elif(n>=6 and n<=20):
    print("Wired")
else:
    print("Not Weird")"""

"""
n = int(input())
i=0

while i<n:
    print(i**2)    #we write square root like this
    i+=1"""




import numpy as np            #eye and identity problem

n, m = map(int, input().split())
output = str(np.eye(n, m))
print(output.replace("0", " 0").replace("1", " 1"))
