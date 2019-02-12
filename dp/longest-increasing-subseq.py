"""
An algorithm to compute the length of the longest increasing subsequence of a given
array of numbers.
"""

import numpy as np

def LIS(arr):
    n = len(arr)
    # add sentinel to beginning of arr
    sentinel = min(arr) - 2
    arr = [sentinel] + arr
    # create memo table
    memo = np.zeros((n+1,n+2))
    """memo[i,j] = length of longest inc subseq in arr[j:] with all terms > arr[i]"""
    # base cases -- memo[_,n] = 0
    for i in range(n+1):
        memo[i,n+1] = 0
    for j in range(1,n+1)[::-1]:
        for i in range(j)[::-1]:
            op1 = 1 + memo[j,j+1]
            op2 = memo[i,j+1]
            if arr[j] <= arr[i]:
                memo[i,j] = op2
            else:
                memo[i,j] = max(op1, op2)
    return memo[0,1]

test_arr = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,7]
print(LIS(test_arr))

test_arr2 = [50, 3, 10, 7, 40, 80]
print(LIS(test_arr2))

# a little nicer way
def LIS2(arr):
    """our subproblem here will be memo[i] = longest inc subseq of arr[i:] that begins with arr[i]"""
    n = len(arr)
    memo = np.zeros(n+1)

    for i in range(n)[::-1]:
        if i == (n-1):
            memo[i] = 1
        else:
            lengths = [0]
            for j in range(i,n):
                if arr[j] > arr[i]:
                    lengths.append(memo[j])
            memo[i] = 1 + max(lengths)
    # returning memo[0] gives longest starting at arr[0]. just taking max gives longest overall
    return max(memo)

print(LIS2(test_arr))
print(LIS2(test_arr2))