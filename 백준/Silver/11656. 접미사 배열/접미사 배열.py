s = input()
arr = []
for i in range(len(s)):
    arr.append(s[i:])

for a in sorted(arr):
    print(a)