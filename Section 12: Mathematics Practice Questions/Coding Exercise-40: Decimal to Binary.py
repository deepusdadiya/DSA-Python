# Problem Description:

# You are given an integer n. Your task is to return its binary 
# representation as a string. Do not use any built-in functions for conversion.

# Input:
# A single integer n, where -10^9 <= n <= 10^9.

# Output:
# A string representing the binary representation of n.

# Example:

# Input: n = 5
# Output: "101"

# Input: n = -5
# Output: "-101"

# Solution:

def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n == 0:
        return "0"
    
    is_negative = n < 0
    n = abs(n)
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    if is_negative:
        binary = "-" + binary

    return binary
    
int_to_binary(-5) 