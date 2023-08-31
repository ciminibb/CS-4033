# CS 4033
# Assignment 1: Hybrid Sort
# Ben Cimini, Blair Bowen, Stetson King

# ALGORITHMS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Bubble Sort
def bubbleSort(arr):
    length = len(arr)

    for numSorted in range(length):
        swapped = False

        for i in range(length - numSorted - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break


# Merge Sort
def mergeSort(ls):
    # Recursive case: list > 1 element.
    if len(ls) > 1:
        # Find midpoint, divide.
        mid = len(ls) // 2
        left, right = ls[:mid], ls[mid:]
        
        # Sort sublists.
        mergeSort(left)
        mergeSort(right)
        
        # MERGE
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




# TESTING
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
x = [4, 0, -1, 1, -99, 68, 60, 68, 2, 3, -98, 200, 111, 101, 3]
mergeSort(x)
print(x)




# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
