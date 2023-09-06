# CS 4033
# Assignment 1: Hybrid Sort
# Ben Cimini, Blair Bowen, Stetson King

import time
import random

# ALGORITHMS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Bubble Sort
def bubbleSort(ls):
    # Sets length
    length = len(ls)

    # Iterates list
    for numSorted in range(length):
        # Sets base case
        swapped = False

        # Iterates through unsorted list
        for i in range(length - numSorted - 1):
            # Swaps elements if elements are out of order
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True
        
        # If nothing was swapped then the list is sorted
        if not swapped:
            break


# Merge Sort
def merge(ls, left, right):
    # Set counters.
    leftIndex = rightIndex = lsIndex = 0
    
    # Iterate sublists.
    while leftIndex < len(left) and rightIndex < len(right):
        # Lesser element to list, increment counter.
        if left[leftIndex] <= right[rightIndex]:
            ls[lsIndex] = left[leftIndex]
            leftIndex += 1
        else:
            ls[lsIndex] = right[rightIndex]
            rightIndex += 1
        
        lsIndex += 1 # always incremented
    
    # Dump leftovers to list.
    while leftIndex < len(left):
        ls[lsIndex] = left[leftIndex]
        leftIndex += 1
        lsIndex += 1
    
    while rightIndex < len(right):
        ls[lsIndex] = right[rightIndex]
        rightIndex += 1
        lsIndex += 1

def mergeSort(ls):
    # Recursive case: list > 1 element.
    if len(ls) > 1:
        # Find midpoint, divide.
        mid = len(ls) // 2
        left, right = ls[:mid], ls[mid:]
        
        # Sort sublists.
        mergeSort(left)
        mergeSort(right)
        
        # Merge sublists.
        merge(ls, left, right)


# Quick Sort
def quickSort(ls):
    if len(ls) <= 1:
        return

    pivot = ls[len(ls) // 2]
    less_than_pivot = [x for x in ls if x < pivot]
    equal_to_pivot = [x for x in ls if x == pivot]
    greater_than_pivot = [x for x in ls if x > pivot]

    quickSort(less_than_pivot)
    quickSort(greater_than_pivot)

    ls.clear()
    ls.extend(less_than_pivot + equal_to_pivot + greater_than_pivot)


# Hybrid Sort
def hybridSort(ls, small, big, threshold):
    # Determine small or big list.
    if len(ls) < threshold:
        # Sort by small-list algorithm.
        if small == 1: # bubble
            bubbleSort(ls)
        
        # No else case for this assignment, only bubble sort!
    
    else:
        # Sort as big-list algorithm.
        if big == 1: # merge
            # Find midpoint, divide.
            mid = len(ls) // 2
            left, right = ls[:mid], ls[mid:]
            
            # Sort sublists.
            hybridSort(left, small, big, threshold)
            hybridSort(right, small, big, threshold)
            
            # Merge sublists.
            merge(ls, left, right)
        
        elif big == 2: # quick
            if len(ls) <= 1:
                return

            pivot = ls[len(ls) // 2]
            less_than_pivot = [x for x in ls if x < pivot]
            equal_to_pivot = [x for x in ls if x == pivot]
            greater_than_pivot = [x for x in ls if x > pivot]

            hybridSort(less_than_pivot, small, big, threshold)
            hybridSort(greater_than_pivot, small, big, threshold)
            
            ls.clear()
            ls.extend(less_than_pivot + equal_to_pivot + greater_than_pivot)

        # No else case for this assignment, only merge and quick sorts!




# TESTING
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Pass/Fail Bubble Sort
def test_bubbleSort():
    # Test case 1: Sorting an empty list should return an empty list.
    input_list = []
    bubbleSort(input_list)
    assert input_list == []

    # Test case 2: Sorting a list with a single element should return the same list.
    input_list = [42]
    bubbleSort(input_list)
    assert input_list == [42]

    # Test case 3: Sorting a list with multiple elements in ascending order.
    input_list = [5, 10, 15, 20, 25]
    bubbleSort(input_list)
    assert input_list == [5, 10, 15, 20, 25]

    # Test case 4: Sorting a list with multiple elements in descending order.
    input_list = [30, 20, 10, 5, 0]
    bubbleSort(input_list)
    assert input_list == [0, 5, 10, 20, 30]

    # Test case 5: Sorting a list with multiple elements in random order.
    input_list = [15, 30, 5, 10, 25]
    bubbleSort(input_list)
    assert input_list == [5, 10, 15, 25, 30]

    # Test case 6: Sorting a list with duplicate elements.
    input_list = [10, 5, 10, 5, 20]
    bubbleSort(input_list)
    assert input_list == [5, 5, 10, 10, 20]

    # Test case 7: Sorting a large list.
    input_list = [i for i in range(1000, 0, -1)]
    bubbleSort(input_list)
    assert input_list == [i for i in range(1, 1001)]


# Pass/Fail Merge Sort
def test_mergeSort():
    # Test case 1: Sorting an empty list should return an empty list.
    input_list = []
    mergeSort(input_list)
    assert input_list == []

    # Test case 2: Sorting a list with a single element should return the same list.
    input_list = [42]
    mergeSort(input_list)
    assert input_list == [42]

    # Test case 3: Sorting a list with multiple elements in ascending order.
    input_list = [5, 10, 15, 20, 25]
    mergeSort(input_list)
    assert input_list == [5, 10, 15, 20, 25]

    # Test case 4: Sorting a list with multiple elements in descending order.
    input_list = [30, 20, 10, 5, 0]
    mergeSort(input_list)
    assert input_list == [0, 5, 10, 20, 30]

    # Test case 5: Sorting a list with multiple elements in random order.
    input_list = [15, 30, 5, 10, 25]
    mergeSort(input_list)
    assert input_list == [5, 10, 15, 25, 30]

    # Test case 6: Sorting a list with duplicate elements.
    input_list = [10, 5, 10, 5, 20]
    mergeSort(input_list)
    assert input_list == [5, 5, 10, 10, 20]

    # Test case 7: Sorting a large list.
    input_list = [i for i in range(1000, 0, -1)]
    mergeSort(input_list)
    assert input_list == [i for i in range(1, 1001)]


# Pass/Fail Quick Sort
def test_quickSort():
    # Test case 1: Sorting an empty list should return an empty list.
    input_list = []
    quickSort(input_list)
    assert input_list == []

    # Test case 2: Sorting a list with a single element should return the same list.
    input_list = [42]
    quickSort(input_list)
    assert input_list == [42]

    # Test case 3: Sorting a list with multiple elements in ascending order.
    input_list = [5, 10, 15, 20, 25]
    quickSort(input_list)
    assert input_list == [5, 10, 15, 20, 25]

    # Test case 4: Sorting a list with multiple elements in descending order.
    input_list = [30, 20, 10, 5, 0]
    quickSort(input_list)
    assert input_list == [0, 5, 10, 20, 30]

    # Test case 5: Sorting a list with multiple elements in random order.
    input_list = [15, 30, 5, 10, 25]
    quickSort(input_list)
    assert input_list == [5, 10, 15, 25, 30]

    # Test case 6: Sorting a list with duplicate elements.
    input_list = [10, 5, 10, 5, 20]
    quickSort(input_list)
    assert input_list == [5, 5, 10, 10, 20]

    # Test case 7: Sorting a large list.
    input_list = [i for i in range(1000, 0, -1)]
    quickSort(input_list)
    assert input_list == [i for i in range(1, 1001)]


# Pass/Fail Hybrid Sort
def test_hybridSort():
    # Test case 1: Sorting an empty list should return an empty list.
    input_list = []
    hybridSort(input_list, small=1, big=1, threshold=10)
    assert input_list == []

    # Test case 2: Sorting a list with a single element should return the same list.
    input_list = [42]
    hybridSort(input_list, small=1, big=1, threshold=10)
    assert input_list == [42]

    # Test case 3: Sorting a list with multiple elements in ascending order (using Merge Sort).
    input_list = [5, 10, 15, 20, 25]
    hybridSort(input_list, small=1, big=1, threshold=10)
    assert input_list == [5, 10, 15, 20, 25]

    # Test case 4: Sorting a list with multiple elements in descending order (using Quick Sort).
    input_list = [30, 20, 10, 5, 0]
    hybridSort(input_list, small=1, big=2, threshold=10)
    assert input_list == [0, 5, 10, 20, 30]

    # Test case 5: Sorting a list with multiple elements in random order (using Merge Sort).
    input_list = [15, 30, 5, 10, 25]
    hybridSort(input_list, small=1, big=1, threshold=10)
    assert input_list == [5, 10, 15, 25, 30]

    # Test case 6: Sorting a list with duplicate elements (using Quick Sort).
    input_list = [10, 5, 10, 5, 20]
    hybridSort(input_list, small=1, big=2, threshold=10)
    assert input_list == [5, 5, 10, 10, 20]

    # Test case 7: Sorting a large list (using Merge Sort).
    input_list = [i for i in range(1000, 0, -1)]
    hybridSort(input_list, small=1, big=1, threshold=10)
    assert input_list == [i for i in range(1, 1001)]


# Performance Tests
def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_sorting_time(sort_function, input_list):
    start_time = time.time()
    sort_function(input_list)
    end_time = time.time()
    return end_time - start_time


# Driver
if __name__ == "__main__":
    # Run pass/fail tests.
    test_bubbleSort()
    print("Bubble Sort tests passed!")
    test_mergeSort()
    print("Merge Sort tests passed!")
    test_quickSort()
    print("Quick Sort tests passed!")
    test_hybridSort()
    print("Hybrid Sort tests passed!")
    print("")
    
    # Run performance tests with different list sizes.
    list_sizes = [100, 1000, 10000, 100000, 1000000]

    for size in list_sizes:
        input_list = generate_random_list(size)
        
        # Get Bubble Sort time.
        bubble_sort_time = measure_sorting_time(bubbleSort, input_list.copy())
        
        # Get Merge Sort time.
        merge_sort_time = measure_sorting_time(mergeSort, input_list.copy())
        
        # Get Quick Sort time.
        quick_sort_time = measure_sorting_time(quickSort, input_list.copy())
        
        # Get Hybrid Sort (Merge) time.
        hybridm_sort_time = measure_sorting_time(lambda lst: hybridSort(lst, small=1, big=1, threshold=100), input_list.copy())
        
        # Get Hybrid Sort (Quick) time.
        hybridq_sort_time = measure_sorting_time(lambda lst: hybridSort(lst, small=1, big=2, threshold=100), input_list.copy())
        
        # Output
        print(f"List size: {size}")
        print(f"Bubble Sort time: {bubble_sort_time} seconds")
        print(f"Merge Sort time: {merge_sort_time} seconds")
        print(f"Quick Sort time: {quick_sort_time} seconds")
        print(f"Hybrid Sort time with Merge: {hybridm_sort_time} seconds")
        print(f"Hybrid Sort time with Quick: {hybridq_sort_time} seconds")
        print("-" * 50)




# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
