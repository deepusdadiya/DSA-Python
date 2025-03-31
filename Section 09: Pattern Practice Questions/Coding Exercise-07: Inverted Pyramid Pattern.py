# Problem Description

# You are given an integer n. Your task is to return an inverted pyramid pattern of '*', where each side has n rows, 
# represented as a list of strings. The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, until the last row has 1 star, with each row centered using spaces.

# Input Parameters:
# n (int): The number of rows in the inverted pyramid.

# Output:
# A list of strings where each string represents a row of the inverted pyramid.

# Example:
# Input: 3
# Output: ['*****', ' *** ', '  *  ']
 
# Input: 5
# Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

# Solution:

def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    string=''
    string_list=[]
    p=n-1
    for i in range(n):
        string=' '*(i)+'*'*(p+p+1)+' '*(i)
        string_list.append(string)
        p=p-1
    print(string_list)
    return string_list
    
generate_inverted_pyramid(5)
