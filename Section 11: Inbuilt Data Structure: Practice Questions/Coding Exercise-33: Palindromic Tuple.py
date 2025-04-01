# Check if Tuple is Palindromic

# Design a Python function named is_palindromic_tuple to check 
# if a tuple is palindromic, meaning it reads the same forwards and backwards.

# Parameters:
# tup (tuple): The input tuple that you need to check for palindromic property.

# Returns:
# True if the tuple is palindromic, False otherwise.

# Example:
# Input: (1, 2, 3, 2, 1)
# Output: True

# Input: ('a', 'b', 'c', 'b', 'a')
# Output: True

# Input: (1, 2, 3, 4, 5)
# Output: False

# Input: ('x', 'y', 'z', 'x')
# Output: False

# Input: ('a',)
# Output: True

# Solution:

def is_palindromic_tuple(tup):
    # Your code goes here
    length=len(tup)
    if length%2==0:
        k=int(length/2)
    else:
        k=int((length+1)/2)
    forward=tup[:k]
    backward=tup[k-1:]
    if forward==backward[::-1]:
        return True
    else:
        return False

is_palindromic_tuple((1, 2, 3, 4, 3, 2, 1))