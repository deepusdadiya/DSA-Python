# Check if All Elements in a List are Unique

# You are given a list of integers. Write a Python program that checks if all elements in the list are unique. 
# If all elements are unique, return True; otherwise, return False.

# Parameters:
# lst (List of integers): The list of integers to check for uniqueness.

# Returns:
# A boolean value True if all elements in the list are unique, False otherwise.

# Example:
# Input: lst = [1, 2, 3, 4, 5]
# Output: True

# Input: lst = [1, 2, 3, 3, 4, 5]
# Output: False

# Solution:

def check_unique(lst):
    # Your code goes here
    unique_list=[]
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)
    if unique_list==lst:
        print("True")
        return True
    else:
        print("False")
        return False

check_unique([1, 2, 3, 4, 5])