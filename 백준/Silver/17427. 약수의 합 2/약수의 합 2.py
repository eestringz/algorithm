n = int(input())
lst = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        lst[j] += i
    lst[i] += lst[i - 1]

print(lst[n])