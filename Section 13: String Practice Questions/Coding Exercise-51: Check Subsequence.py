# Problem Description:

# You are given two strings s and t. Your task is to determine 
# if string t is a subsequence of string s. A subsequence of a string 
# is a new string that is formed from the original string by deleting some 
# (or no) characters without changing the order of the remaining characters.

# Input:
# Two strings s and t where the length of s is between 1 and 1000, 
# and the length of t is between 1 and 1000.

# Output:
# Return True if t is a subsequence of s, and False otherwise.

# Example:

# Input: s = "abcde", t = "ace"
# Output: True

# Input: s = "abcde", t = "aec"
# Output: False

# Solution:

def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    # Your code here
    s_index, t_index = 0, 0
    if len(t) == 0:
        return True
    if len(s) == 0:
        return False
    if len(s) < len(t):
        return False
    for i in s:
        if s_index == len(s):
            break
        if i == t[t_index]:
            t_index += 1
        s_index += 1
    if t_index == len(t):
        return True
    else:
        return False
        
is_subsequence("abcde", "aec")