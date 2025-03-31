# Diamond Pattern
# Problem Description:

# You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part 
# (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.

# Input:
# A single integer n, where 1 <= n <= 100.

# Output:
# A list of strings where each string represents a row in the diamond pattern.

# Example:
# Input: 3
# Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
# Input: 5
# Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

# Solution:

def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    string=''
    string_list=[]
    p=n-1
    for i in range(n):
        string = ' '*(p) + '*' * (i+i+1) + ' '*(p)
        string_list.append(string)
        p=p-1
    p=1
    for i in range(n-2, -1, -1):
        string = ' ' * p + '*' * (2 * i + 1) + ' ' * p
        string_list.append(string)
        p=p+1
    print(string_list)
    return string_list

generate_diamond(5)
