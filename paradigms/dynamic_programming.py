"""
Module 6: Dynamic Programming Paradigm
Optimize calculations by breaking them into overlapping subproblems and storing sub-results.
"""

def optimize_truck_loading(capacity: int, weights: list[int], values: list[int]) -> int:
    """
    Maximizes the total value of items loaded into a truck without exceeding capacity.
    This is the classic 0/1 Knapsack problem.
    
    Arguments:
    capacity -- Maximum weight the truck can hold
    weights  -- List containing the weight of each package
    values   -- List containing the dollar value of each package
    
    TODO:
    1. Create a 2D DP table of size (num_items + 1) x (capacity + 1) initialized to 0.
    2. Loop through every item and every capacity unit.
    3. For each cell, determine if including the current item yields a higher value 
       than excluding it.
    4. Return the maximum value found at table[num_items][capacity].
    
    Time Complexity Expected: O(n * capacity)
    """
    num_items = len(weights)
    # YOUR CODE HERE
    pass
