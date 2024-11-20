"""Remove Duplicates*  
   Given a list with duplicate elements, write a function to return a list of unique elements.  
   Input: [1, 2, 2, 3, 4, 4, 5]  
   Output: [1, 2, 3, 4, 5]
"""


def remove_duplicates(a):

    return list(set(a))

a=[1,2,2,3,3,4,4,5,5]

unique_elements= remove_duplicates(a)
print(unique_elements)