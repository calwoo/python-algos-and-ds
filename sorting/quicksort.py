"""
Quicksort -- sorting algorithm using divide-and-conquer
    INPUT
        array
    OUTPUT
        array ordered in ascending order
    RUNTIME
        O(n*log n) - time
        O(n) - space
"""

def quicksort(arr):
    # base case
    if len(arr) < 2:
        return arr
    # choose first element as pivot
    pivot = arr[0]
    # partition arr
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    # inductive return
    return quicksort(left) + [pivot] + quicksort(right)

test = [8, 5, 7, 1, 9, 3]
print(quicksort(test))
test2 = [5, 3, 6, 2, 10]
print(quicksort(test2))