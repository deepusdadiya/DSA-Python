# Rotate a List (Without Slicing)

# You are given a list of integers and an integer k. 
# Write a Python function to rotate the list to the right by k positions 
# without using slicing. A rotation shifts elements from the end of the list to the front.

# Parameters:
# lst (List of integers): The list to be rotated.
# k (Integer): The number of positions to rotate the list.

# Returns:
# A list of integers rotated by k positions.

# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Input: lst = [10, 20, 30, 40, 50], k = 3
# Output: [30, 40, 50, 10, 20]

# Solution:

def rotate_list(lst, k):
    # Your code goes here
    if k <= len(lst):
        lst1=[]
        p=-k
        length = len(lst)
        for i in lst:
            i=lst[p]
            lst1.append(i)
            p=p+1
    elif k > len(lst):
        lst1=[]
        p=len(lst)-k
        length = len(lst)
        for i in lst:
            i=lst[p]
            lst1.append(i)
            p=p+1
    print(lst1)
    return lst1
    
rotate_list([1, 2, 3, 4, 5, 6], 8)