"""
Module 6: Divide and Conquer Paradigm
Break down a large list into smaller sub-problems, solve them, and merge.
"""

def divide_and_conquer_sort(manifest_ids: list[int]) -> list[int]:
    """
    Sorts a list of shipping manifest IDs in ascending order.
    
    TODO:
    1. Base Case: If the list length is 0 or 1, it is already sorted. Return it.
    2. Divide: Find the midpoint and split the list into left and right sub-lists.
    3. Conquer: Recursively call divide_and_conquer_sort on both halves.
    4. Combine: Merge the two sorted halves back into a single sorted list.
    
    Do NOT use Python's built-in .sort() or sorted().
    """
    # YOUR CODE HERE
    pass

def _merge(left: list[int], right: list[int]) -> list[int]:
    """Helper function to merge two sorted arrays cleanly into one sorted output."""
    # YOUR CODE HERE
    pass
