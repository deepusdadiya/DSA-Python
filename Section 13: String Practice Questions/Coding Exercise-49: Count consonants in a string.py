# Problem Description:

# You are given a string s. Your task is to count the number of consonants 
# in the string and return the total count. A consonant is any alphabetic character
#  that is not a vowel (a, e, i, o, u).

# Input:
# A single string s, where the length of s is between 1 and 1000.

# Output:
# An integer representing the total count of consonants in the input string.

# Example:

# Input: "Hello, World!"
# Output: 7

# Input: "Python Programming"
# Output: 13

# Solution:

def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    vowels='aeiouAEIOU'
    s = s.replace(' ', '')
    total_const_count=0
    for i in s:
        if i.isalpha() and i not in vowels:
            print(i)
            total_const_count = total_const_count + 1
    print(total_const_count)
    return total_const_count
    
count_consonants("aeiou")