n = int(input())
arr = []
for _ in range(n):
    name, dd, mm, yy = input().split()
    arr.append([name, int(dd), int(mm), int(yy)])

arr.sort(key=lambda x: (x[3], x[2], x[1]))

print(arr[-1][0])
print(arr[0][0])