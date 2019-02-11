"""
A symphony tour of the Fibonacci sequence, in 3 movements.
"""

import timeit

# adagio -- naive recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))