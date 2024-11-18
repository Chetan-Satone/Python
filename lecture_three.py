""" concatention

"hello" + "world" = "helloworld"

length of str
 
len(str)

Indexing start from 0

string access

str[1:4]
str[:4]
str[1:]

Slicing

negative index    str[-3:-1]  starting from right side from -1"""


"""str = "I am decoder."

print(str.endswith("e."))

print(str.capitalize())

print(str.replace("a", "u"))

print(str.find("I"))

print(str.count(str))"""

"""movie = []
a = input("write your movie name:")
movie.append(a)
a = input("write your movie name: ")
movie.append(a)
a = input("Write your movie name: ")
movie.append(a)

print(movie)"""


a = [1,2,3,2,1]
b = [1,2,3]

a_list = a.copy()
a_list.reverse()



if(a_list == a):
    print("is palindrome")
else:
    print("not palindrome")    
