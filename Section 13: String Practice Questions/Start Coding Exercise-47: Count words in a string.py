# Problem Description:

# You are given a string s. Your task is to count the number of words 
# in the string and return the total count. A word is defined as a sequence of characters separated by spaces.

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# An integer representing the total count of words in the input string.

# Example:
# Input: "Hello, World!"
# Output: 2

# Input: "Python programming is fun."
# Output: 4

# Solution:

def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    if len(s)>0:
        s=s.split(' ')
        filtered_lst = [item for item in s if item != '']
        print(filtered_lst)
        count=len(filtered_lst)
        print(count)
        return count
    elif len(s)==0:
        count=0
        return count
count_words("Hello,   World!")