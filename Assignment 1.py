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


# TESTING
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
