"""Frequency Counter*  
   Write a Python function to count the frequency of each character in a given string and store it in a dictionary.  
   Input: "hello world"  
   Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
"""


int = "hello world"
frequency = {}

for char in int:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
res= frequency

print(frequency)