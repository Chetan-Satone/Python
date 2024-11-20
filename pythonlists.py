""" Write a function that accepts a list of integers and returns the second largest number.  
   Input: [3, 1, 4, 1, 5, 9]  
   Output: 5
"""


def find_second_largest(numbers):
    return sorted(set(numbers))[-2]

# Example usage
numbers = [3,1,4,1,5,9]
print("The second largest number is:", find_second_largest(numbers))