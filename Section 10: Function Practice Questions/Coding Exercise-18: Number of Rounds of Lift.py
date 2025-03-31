def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    for i in range(n+1):
        number_of_rounds = n/capacity
        if number_of_rounds.is_integer():
            number_of_rounds = int(number_of_rounds)
        else:
            number_of_rounds = int(number_of_rounds)+1
    print(number_of_rounds)
    return number_of_rounds
    
calculate_lift_rounds(8, 4)