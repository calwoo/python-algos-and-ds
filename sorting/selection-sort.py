"""
Selection sort -- we swap the top element with the smallest element in the rest of the list
    INPUT
        array
    OUTPUT
        sorted array in ascending order
    RUNTIME
        O(n^2) - time
        O(1) - space
"""

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = arr[i]
        smallest_index = i
        for j in range(i, len(arr)):
            # find smallest in arr[i:]
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        # swap top and smallest
        temp = arr[i]
        arr[i] = smallest
        arr[smallest_index] = temp
    return arr

test = [8, 5, 7, 1, 9, 3]
print(selection_sort(test))
test2 = [5, 3, 6, 2, 10]
print(selection_sort(test2))

# the following is an implementation with O(n) space
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort_two(arr):
    return_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        return_arr.append(arr.pop(smallest))
    return return_arr

