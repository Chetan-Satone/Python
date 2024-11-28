def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
print(f"{string} is a palindrome: {is_palindrome(string)}")