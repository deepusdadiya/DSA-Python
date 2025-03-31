# Number Pyramid Pattern
# Problem Description:

# You are given an integer n. Your task is to return a pyramid pattern of numbers, 
# where each row contains increasing numbers starting from 1 up to the row number, 
# and the pyramid is centered with leading spaces.

# Input:
# A single integer n, where 1 <= n <= 100.

# Output:
# A list of strings where each string represents a row in the pyramid pattern.

# Example:
# Input: 4
# Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
# Input: 3
# Output: ['  1  ', ' 1 2 ', '1 2 3']

# Solution:

def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    string=''
    string_list=[]
    p=n-1
    for i in range(n):
        if i == 0:
            string = ' '*p + str(i+1) + ' '*p
            string_list.append(string)
            string = '1'
            p=n-2
        if i != 0:
            string= ' '*p + string + ' ' + str(i+1) + ' '*p
            string_list.append(string)
            string = string.strip()
            p=p-1
    print(string_list)
    return string_list
    
generate_number_pyramid(7)
