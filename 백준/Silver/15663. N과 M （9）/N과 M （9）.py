from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

paths = set(permutations(lst, m))

for path in paths:
    print(' '.join(map(str, path)))