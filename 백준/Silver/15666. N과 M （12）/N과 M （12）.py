from itertools import combinations_with_replacement

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

paths = set(combinations_with_replacement(lst, m))
for path in paths:
    print(' '.join(map(str, path)))