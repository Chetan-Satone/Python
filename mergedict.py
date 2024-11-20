"""Merge Dictionaries*  
   Given two dictionaries, write a program to merge them. If there are common keys, add their values.  
   Input: {'a': 10, 'b': 20} and {'b': 30, 'c': 40}  
   Output: {'a': 10, 'b': 50, 'c': 40}
"""


int={'a': 10, 'b': 20} 
var ={'b': 30, 'c': 40}


add= {**int,**var}


print(add)

