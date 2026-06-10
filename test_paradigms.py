import pytest
from paradigms.brute_force import find_exact_valuation_pair
from paradigms.divide_conquer import divide_and_conquer_sort
from paradigms.dynamic_programming import optimize_truck_loading

def test_brute_force_pair_matching():
    prices = [10, 25, 40, 75, 50]
    
    # Pair adding up to 90 is 40 (idx 2) and 50 (idx 4)
    assert find_exact_valuation_pair(prices, 90) == (2, 4)
    # Missing pair match
    assert find_exact_valuation_pair(prices, 1000) is None

def test_divide_and_conquer_sorting():
    unsorted_manifests = [909, 101, 404, 202, 707, 303]
    expected_sorted = [101, 202, 303, 404, 707, 909]
    
    assert divide_and_conquer_sort(unsorted_manifests) == expected_sorted

def test_dynamic_programming_knapsack():
    # Truck can hold 50kg maximum
    truck_capacity = 50
    package_weights = [10, 20, 30]
    package_valuations = [60, 100, 120]
    
    # Best combination: Item 2 and Item 3 (Weight: 20+30=50, Value: 100+120=220)
    max_profit = optimize_truck_loading(truck_capacity, package_weights, package_valuations)
    assert max_profit == 220
