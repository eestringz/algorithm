import sys

input = sys.stdin.readline

S, P = map(int, input().split())
lst = list(input().strip())
a, c, g, t = list(map(int, input().split()))
dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(P):
    dic[lst[i]] += 1
cnt = 0
for start in range(S - P + 1):
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        cnt += 1
    if start + P < S:
        dic[lst[start]] -= 1
        dic[lst[start + P]] += 1

print(cnt)