# Check if a List is a Subset of Another List (Brute Force Approach)

# You are given two lists of integers. Write a Python program that 
# checks whether the first list is a subset of the second list using 
# a brute-force approach, without using the in keyword. 
# A list is considered a subset if all elements of the first list are present in the second list.

# Parameters:

# lst1 (List of integers): The first list, which is being checked as a subset.
# lst2 (List of integers): The second list, which is the list to compare against.

# Returns:
# A boolean value True if lst1 is a subset of lst2, otherwise False.

# Example:
# Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
# Output: True
# All elements in lst1 are present in lst2.

# Input: lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]
# Output: False
# The element 6 is not present in lst2

# Solution:

def is_subset(lst1, lst2):
    # Your code goes here
    for i in lst1:
        if i not in lst2:
            return False
    return True

is_subset([1, 6], [1, 2, 3, 4, 5])