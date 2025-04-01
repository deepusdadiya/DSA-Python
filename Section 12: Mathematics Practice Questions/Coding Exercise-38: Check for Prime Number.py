# Problem Description:

# You are given an integer n. Your task is to check whether 
# the number is prime or not. A prime number is a number greater 
# than 1 that has no divisors other than 1 and itself. 
# Return True if the number is prime, and False otherwise.

# Input:
# A single integer n where 1 <= n <= 10^6.

# Output:
# Return True if n is a prime number, otherwise return False.

# Example:
# Input: n = 5
# Output: True

# Input: n = 4
# Output: False

# Solution:

def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

is_prime(26)