import numpy as np

# recursive solution

def subset_sum(arr, target):
    n = len(arr)
    memo = np.zeros((n+1, target+1))

    # here memo[i,t] = True when some subset of arr[i:] sums to t
    # at the end, memo[n,t] = False as here arr[n:] is empty
    for t in range(target+1):
        memo[n,t] = 0
    # step down through i
    for i in range(n)[::-1]:
        memo[i,0] = 1
        # when t is less than arr[i], we can skip arr[i]
        for t in range(1,min(arr[i], target)):
            memo[i,t] = memo[i+1, t]
        for t in range(min(arr[i], target), target):
            memo[i,t] = memo[i+1, t] or memo[i+1, t-arr[i]]
    print(memo)
    return memo[0,t]

arr = [5,4,1,3,2]
print(subset_sum(arr, 6))