# Sandglass Pattern
# Problem Description:

# You are given an integer n. Your task is to return a sandglass pattern of '*', 
# where the first row contains 2n - 1 stars and each subsequent row decreases the number of stars by 2, 
# until the last row contains a single star. After reaching the smallest width, the pattern then continues 
# with the same number of stars increasing back to 2n - 1. The stars in each row should be centered.

# Input:
# A single integer n, where 1 <= n <= 100.

# Output:
# A list of strings where each string represents a row in the sandglass pattern.

# Example:
# Input: 3
# Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
 
# Input: 4
# Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']

# Solution:

def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    string=''
    string_list=[]
    q=n+n-1
    p=0
    for i in range(n):
        string = ' '*p + '*'*(q) + ' '*p
        string_list.append(string)
        p=p+1
        q=q-2
        continue
    r=3
    s=n-2
    for i in range(n+1, n+n):
        string = ' '*s + '*'*(r) + ' '*s
        string_list.append(string)
        s=s-1
        r=r+2
    print(string_list)
    return string_list

generate_sandglass(5)
