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




# TESTING AND PERFORMANCE COMMENTS
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
    list_sizes = [100, 1000, 10000]

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


# Performance Comments
"""
Set 1
--------------------------------------------------
List size: 100
Bubble Sort time: 0.0009980201721191406 seconds
Merge Sort time: 0.0009970664978027344 seconds
Quick Sort time: 0.0 seconds
Hybrid Sort time with Merge: 0.0 seconds
Hybrid Sort time with Quick: 0.000997304916381836 seconds
--------------------------------------------------
List size: 1000
Bubble Sort time: 0.11332464218139648 seconds
Merge Sort time: 0.003995656967163086 seconds
Quick Sort time: 0.0029938220977783203 seconds
Hybrid Sort time with Merge: 0.0069844722747802734 seconds
Hybrid Sort time with Quick: 0.006974935531616211 seconds
--------------------------------------------------
List size: 10000
Bubble Sort time: 12.056044816970825 seconds
Merge Sort time: 0.05388998985290527 seconds
Quick Sort time: 0.022930622100830078 seconds
Hybrid Sort time with Merge: 0.10032939910888672 seconds
Hybrid Sort time with Quick: 0.06534981727600098 seconds
--------------------------------------------------

Set 2
--------------------------------------------------
List size: 100
Bubble Sort time: 0.0009965896606445312 seconds
Merge Sort time: 0.0 seconds
Quick Sort time: 0.0 seconds
Hybrid Sort time with Merge: 0.0009970664978027344 seconds
Hybrid Sort time with Quick: 0.0 seconds
--------------------------------------------------
List size: 1000
Bubble Sort time: 0.11632204055786133 seconds
Merge Sort time: 0.003985166549682617 seconds
Quick Sort time: 0.0030317306518554688 seconds
Hybrid Sort time with Merge: 0.006982564926147461 seconds
Hybrid Sort time with Quick: 0.0069849491119384766 seconds
--------------------------------------------------
List size: 10000
Bubble Sort time: 12.003134489059448 seconds
Merge Sort time: 0.05447793006896973 seconds
Quick Sort time: 0.02689361572265625 seconds
Hybrid Sort time with Merge: 0.1022801399230957 seconds
Hybrid Sort time with Quick: 0.06541848182678223 seconds
--------------------------------------------------

Set 3
--------------------------------------------------
List size: 100
Bubble Sort time: 0.0019948482513427734 seconds
Merge Sort time: 0.0 seconds
Quick Sort time: 0.000997781753540039 seconds
Hybrid Sort time with Merge: 0.0 seconds
Hybrid Sort time with Quick: 0.0010182857513427734 seconds
--------------------------------------------------
List size: 1000
Bubble Sort time: 0.11334538459777832 seconds
Merge Sort time: 0.003979921340942383 seconds
Quick Sort time: 0.002994060516357422 seconds
Hybrid Sort time with Merge: 0.006946563720703125 seconds
Hybrid Sort time with Quick: 0.008016824722290039 seconds
--------------------------------------------------
List size: 10000
Bubble Sort time: 11.866494417190552 seconds
Merge Sort time: 0.053893089294433594 seconds
Quick Sort time: 0.021982192993164062 seconds
Hybrid Sort time with Merge: 0.09934115409851074 seconds
Hybrid Sort time with Quick: 0.061417341232299805 seconds
--------------------------------------------------

Comparison
--------------------------------------------------
The following discussion is based on the test sets above. In each set, all
algorithms were run on the same, randomly-generated lists. Let's begin with the
obvious, the recursive algorithms were faster than bubble sort for all lists.
Of course, the observed difference was negligible for small lists, but it
increased exponentially with larger lists. A more interesting comparison is
that of merge, quick, and hybrid sorts. Focusing on merge and quick, first, the
results show the quick sort is more efficient. There are a few counterexamples,
but only for small lists. The largest lists we tested were of size 10000, for
which quick sort was approximately 0.0302 seconds and 55.78% faster on average.
So, was that speed difference carried on through hybrid sort? For large lists,
hybrid sort was fastest when quick sort was its recursive component. However,
there was no significant difference for medium or small lists. Let's dig into
that statement. Note, in this case, a "medium" list has 1000 elements and a
"small" list has 100. For medium lists, the total aggregate difference was only
0.00107 seconds (in favor of hybrid/merge, actually). That result was even more
negligible for small lists. On large lists, though, hybrid/quick was 36.38%
faster on average. Finally, it should be noted that either hybrid sort is
slower than both merge and quick sorts by themselves. This was observed across
all list sizes. It goes to show, when sorting lists, recursion is the way.
"""




# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
"""
The task environment of sorting a list is as follows.

Bubble Sort
--------------------------------------------------
P: Sort a giving list of elements
E: List of elements
A: Swap elements in the list
S: Values & position of elements

Bubble sort is a simple reflex agent. For any given comparison, the "world" of
the algorithm contains only the pair of elements. With only that knowledge, it
acts on a given condition (if left <= right).

Merge Sort
--------------------------------------------------
P: Sort a giving list of elements
E: List of elements
A: Divide list of elements, Merge list together in a sorted manner
S: Values & position of elements and sublists

Merge sort is a reflex agent with state. As the algorithm recurses, frames of
its world are kept on a stack. In other words, it keeps track of how the world
evolves. Not only that, it later uses that knowledge to merge the frames. That
being said, merge sort does not look forward upon the impact of its actions. It
only acts on the conditions it was given.

Quick Sort
--------------------------------------------------
P: Sort a giving list of elements
E: List of elements
A: Select pivot, Partition list by swapping elements
S: Values & position of elements, sublists, pivot

Quick sort is a reflex agent with state. The role of recursion in that statement
is the same as for merge sort, see the above discussion. I'll add, though, that
the algorithm has no goals or concept of utility. A programmer may want
efficiency, but the algorithm itself isn't concerned with making itself any
faster.
"""
