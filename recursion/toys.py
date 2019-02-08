def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

# countdown(10)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

print(sum([2,4,6]))