# Program to Reverse a List
# Reverse a List (Non-Slicing Approach)

# You are given a list of integers. Write a Python program that 
# reverses the list without using slicing (lst[::-1]). 
# The program should return the reversed list.

# Parameters:
# lst (List of integers): The list of integers to be reversed.

# Returns:
# A list of integers where the order of elements is reversed from the input list.

# Example:
# Input: lst = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# Solution:

def reverse_list(lst):
    # Your code goes here
    lst2 = []
    length = len(lst)
    if length > 1:
        for i in lst:
            i = lst[length-i]
            lst2.append(i)
        print(lst2)
        return lst2
    elif length == 1:
        for i in lst:
            lst2.append(i)
        print(lst2)
        return lst2
    elif length == 0:
        for i in lst:
            lst2.append(i)
        print(lst2)
        return lst2
        
reverse_list([1, 2, 3, 4, 5])