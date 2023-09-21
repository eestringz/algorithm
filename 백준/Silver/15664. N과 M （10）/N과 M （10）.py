from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

paths = set(combinations(lst, m))

for path in paths:
    print(' '.join(map(str, path)))