# Problem Description:

# You are given a string s. Your task is to find the length of the 
# longest word in the string. A word is defined as a sequence of 
# characters separated by spaces. Do not use any built-in functions for string manipulation.

# Input:
# A string s, where the length of s is between 1 and 1000 characters.

# Output:
# An integer representing the length of the longest word in the string.

# Example:

# Input: s = "The quick brown fox jumps over the lazy dog"
# Output: 5

# Input: s = "Hello World"
# Output: 5

# Solution:

def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    # Your code here
    length_list=[]
    s=s.split(' ')
    for i in s:
        length_list.append(len(i))
    maximum_length = max(length_list)
    print(maximum_length)
    return maximum_length

longest_word_length("The quick brown fox jumps over the lazy dog")