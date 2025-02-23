import sys

from itertools import combinations

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mbtis = input().split()
    min_diff = 1000
    
    if N > 32:
        print(0)
    else:
        for i in combinations(mbtis, 3):
            a, b, c = i
            diff = 0
            diff += len(set(a) - set(b))
            diff += len(set(b) - set(c))
            diff += len(set(c) - set(a))
            min_diff = min(diff, min_diff)

        print(min_diff)
