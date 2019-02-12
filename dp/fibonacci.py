"""
A symphony tour of the Fibonacci sequence, in 3 movements.
"""

# adagissimo -- naive recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# adagio -- memoize a bit
cache = {}

def mem_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n not in cache.keys():
            cache[n] = mem_fibonacci(n-1) + mem_fibonacci(n-2)
        return cache[n]

print(mem_fibonacci(10))
print(mem_fibonacci(100))
print(mem_fibonacci(1000))
# doesn't even break a sweat

# allegretto -- loop
def iter_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_1 = 0
        prev_2 = 1
        for _ in range(2,n):
            sum = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = sum
        return prev_1 + prev_2

print(iter_fibonacci(10))
print(iter_fibonacci(100))
print(iter_fibonacci(1000))