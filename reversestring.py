def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
