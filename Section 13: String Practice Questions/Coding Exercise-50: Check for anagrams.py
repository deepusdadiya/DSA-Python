# Problem Description:

# You are given two strings s and t. Your task is to determine 
# if string t is an anagram of string s. An anagram is a word or phrase 
# formed by rearranging the characters of a different word or phrase, 
# using all the original characters exactly once.

# Input:
# Two strings s and t where both lengths are between 1 and 1000.

# Output:
# Return True if t is an anagram of s, and False otherwise.

# Example:

# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False

# Solution:

def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    s = sorted(s)
    t = sorted(t)
    if s == t:
        print("True")
        return True
    else:
        print("Flase")
        return False

is_anagram("rat", "cat")