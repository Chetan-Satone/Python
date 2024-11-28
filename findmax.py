def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

numbers = [10, 20, 45, 2, 99, 65]
print("Largest number:", find_largest(numbers))