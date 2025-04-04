# Problem Description:

# You are given two strings, s and t. Your task is to determine 
# if the string t is a substring of the string s. A substring is 
# a contiguous sequence of characters within a string. 
# Do not use any built-in functions for string operations 
# and do not use recursion.

# Input:
# Two strings s and t, where 1 <= len(s), len(t) <= 1000.

# Output:
# A boolean value (True or False) indicating whether t is a substring of s.

# Example:

# Input: s = "hello world", t = "world"
# Output: True

# Input: s = "hello world", t = "worlds"
# Output: False

# Solution:

def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            return True
    return False
    
is_substring("hello world", "llow")