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
# def partition(arr, first, last, start, mid):
     
#     pivot = arr[last]
#     end = last
     
#     # Iterate while mid is not greater than end.
#     while (mid[0] <= end):
         
#         # Inter Change position of element at the starting if it's value is less than pivot.
#         if (arr[mid[0]] < pivot):
             
#             arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
             
#             mid[0] = mid[0] + 1
#             start[0] = start[0] + 1
             
#         # Inter Change position of element at the end if it's value is greater than pivot.
#         elif (arr[mid[0]] > pivot):
             
#             arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
             
#             end = end - 1
             
#         else:
#             mid[0] = mid[0] + 1
 
# # Function to sort the array elements in 3 cases
# def quicksort(arr,first,last):
#     # First case when an array contain only 1 element
#     if (first >= last):
#         return
     
#     # Second case when an array contain only 2 elements
#     if (last == first + 1):
         
#         if (arr[first] > arr[last]):
             
#             arr[first], arr[last] = arr[last], arr[first]
             
#             return
 
#     # Third case when an array contain more than 2 elements
#     start = [first]
#     mid = [first]
 
#     # Function to partition the array.
#     partition(arr, first, last, start, mid)
     
#     # Recursively sort sublist containing elements that are less than the pivot.
#     quicksort(arr, first, start[0] - 1)
 
#     # Recursively sort sublist containing elements that are more than the pivot
#     quicksort(arr, mid[0], last)

def quickSort(arr):
    if len(arr) <= 1:
        return

    pivot = arr[len(arr) // 2]
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    quickSort(less_than_pivot)
    quickSort(greater_than_pivot)

    arr.clear()
    arr.extend(less_than_pivot + equal_to_pivot + greater_than_pivot)

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
w = [8, -3, 12, -6, 17, 5, -10, 14, 9, -1, 19, 4, 8, -3, 12, -6, 17, 5, -10, 14, 9, -1, 19, 4]
quickSort(w)
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
hybridSort(z2, 1, 2, 4)
print(z2)




# QUESTIONS
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
