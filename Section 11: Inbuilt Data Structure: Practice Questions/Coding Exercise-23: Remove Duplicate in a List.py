# Remove Duplicate in a List
# Remove Duplicates from a List

# You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

# Parameters:
# lst (List of integers): The list of integers from which duplicates should be removed.

# Returns:
# A list of integers where all duplicates have been removed, preserving the original order.

# Example:
# Input: lst = [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Input: lst = [4, 5, 5, 4, 6, 7]
# Output: [4, 5, 6, 7]

# Solution:

def remove_duplicates(lst):
    # Your code goes here
    empty_list=[]
    for i in lst:
        if i not in empty_list:
            empty_list.append(i)
    print(empty_list)
    return empty_list

remove_duplicates([4, 5, 5, 4, 6, 7])