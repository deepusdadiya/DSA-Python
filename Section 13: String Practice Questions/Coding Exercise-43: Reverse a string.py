# Problem Description:
# You are given a string s. Your task is to return the reversed version of the string.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# A single string that is the reverse of the input string.

# Example:
# Input: "hello"
# Output: "olleh"

# Input: "Python"
# Output: "nohtyP"

# Solution:

def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here
    print(s[::-1])
    return s[::-1]

reverse_string("hello")