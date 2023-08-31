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
def merge(arr, lowest, middle, highest):
    # Set "position trackers."
    leftIndex = lowest
    rightIndex = middle + 1
    
    # Initialize temporary list.
    temp = []
    
    # Iterate left and right sublists.
    while leftIndex <= middle and rightIndex <= highest:
        # Add lesser element to temporary list and increment tracker.
        if arr[leftIndex] <= arr[rightIndex]:
            temp += [arr[leftIndex]]
            leftIndex += 1
        else:
            temp += [arr[rightIndex]]
            rightIndex += 1
    
    # Dump leftover sublist elements to temporary list.
    while leftIndex <= middle: # will skip if traversed
        temp += [arr[leftIndex]]
        leftIndex += 1

    while rightIndex <= highest: # will skip if traversed
        temp += [arr[rightIndex]]
        rightIndex += 1
    
    # Copy temporary list to original list.
    j = 0
    for i in range(lowest, highest + 1):
        arr[i] = temp[j]
        j += 1

def mergeSort(arr, lowest, highest):
    # Recursive case: sublist > 1 element.
    if lowest < highest:
        # Find midpoint.
        middle = (lowest + highest) // 2
        
        # Sort left and right sublists.
        mergeSort(arr, lowest, middle)
        mergeSort(arr, middle + 1, highest)
        
        # Merge sublists.
        merge(arr, lowest, middle, highest)




# TESTING
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
ls = [1, 6, 2, 8, 9, 56, 23, 0, -5, 6, 45, 69, 2, 67, 100000, -22222, 13, 13]
mergeSort(ls, 0, 17)
print(ls)




# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
