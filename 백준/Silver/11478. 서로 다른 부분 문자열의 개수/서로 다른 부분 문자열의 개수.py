s = list(input())
lst = set()
for i in range(len(s)):
    for k in range(1, len(s) - i + 1):
        lst.add(''.join(s[i:i + k]))
print(len(lst))