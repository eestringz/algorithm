n, l = map(int, input().split())
lst = list(map(int, input().split()))

for i in sorted(lst):
    if l >= i:
        l += 1

print(l)