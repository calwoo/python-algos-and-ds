"""
Binary search --
    INPUT
        ordered array of elements and a key
    OUTPUT
        index matching key
    RUNTIME
        O(log n) - time
        O(1) - space
"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = arr[mid]
        if guess == key:
            return mid
        elif guess > key:
            high = mid - 1
        else:
            low = mid + 1
    return None

test = [1,2,3,5,7,11,13]
print(binary_search(test, 4))
print(binary_search(test, 11))