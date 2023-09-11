import math


def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1


def solve(n):
    if len(str(n)) == N:
        print(n)
    for i in range(10):
        if isprime(n * 10 + i):
            solve(n * 10 + i)


N = int(input())
solve(2)
solve(3)
solve(5)
solve(7)