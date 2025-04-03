# Problem Description:

# You are given two integers n and m. Your task is to find the GCD 
# of these two numbers. The GCD is the largest positive integer 
# that divides both numbers without leaving a remainder. 
# Do not use any built-in functions and do not use recursion.

# Input:
# Two integers n and m, where 1 <= n, m <= 10^9.

# Output:
# An integer representing the GCD of n and m.

# Example:
# Input: n = 48, m = 18
# Output: 6

# Input: n = 56, m = 98
# Output: 14

# Solution:

def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    gcd=1
    for i in range(1, min(n, m)+1):
        if n%i == 0 and m%i==0:
            gcd=i
    print(gcd)
    return gcd

gcd(15, 15)
