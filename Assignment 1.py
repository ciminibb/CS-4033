# CS 4033
# Assignment 1: Hybrid Sort
# Ben Cimini, Blair Bowen, Stetson King

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
def partition(ls, low, high):
    # Use first element as pivot
    pivot = ls[low]
    left = low + 1
    right = high

    done = False
    while not done:
        # While left and right don't cross and element doesn't belong on this side
        while left <= right and ls[left] <= pivot:
            left = left + 1
        while right >= left and ls[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            ls[left], ls[right] = ls[right], ls[left]
    # Swap pivot where elements less than pivot and more than pivot meet
    ls[low], ls[right] = ls[right], ls[low]

    # Return index
    return right

def quickSort(ls, low, high):
    if low < high:
        pivot_index = partition(ls, low, high)

        quickSort(ls, low, pivot_index)
        quickSort(ls, pivot_index + 1, high)

# Hybrid Sort
stackTrack = []
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
            low, high = 0, len(ls) - 1
            if low < high:
                pivot_index = partition(ls, low, high)

                left, right = ls[:pivot_index + 1], ls[pivot_index + 1:]

                hybridSort(left, small, big, threshold)
                hybridSort(right, small, big, threshold)

                ls[:] = left + right

        # No else case for this assignment, only merge and quick sorts!




# TESTING
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
w = [8, -3, 12, -6, 17, 5, -10, 14, 9, -1, 19, 7, -4, 11, 2]
quickSort(w, 0, 14)
print(w)

x = [4, 0, -1, 1, -99, 68, 60, 68, 2, 3, -98, 200, 111, 101, 3]
mergeSort(x)
print(x)

y = [1, 8, 2, 19, -30, 31, -32, 0, 5, 6, 4, 0]
bubbleSort(y)
print(y)

z = [3, 9, 4, 5, 0, 1, -2, -3, -4, 5, 18, 800, 799, 10, 13, 12, 11]
hybridSort(z, 1, 1, 4)
print(z)

z2 = [5, -12, 8, 0, -3, 17, -9, 25, -6, 10, -15, 7, -1, 4, -20]
# z2 = [4, 0, -1, 1, -99, 68, 60, 68, 2, 3, -98, 200, 111, 101, 3]
hybridSort(z2, 1, 2, 4)
print(z2)




# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
