import sys

input = sys.stdin.readline

N = int(input())
genes = input().split()

ans = set()

for x in range(ord('A'), ord('Z') + 1):
    x_char = chr(x)
    cnt = sum(1 for gene in genes if gene[0] == x_char)

    if cnt > 1:
        for gene in genes:
            ans.add(max(x_char, gene[1]))
    elif cnt == 1:
        for gene in genes:
            if gene[0] == x_char: continue
            ans.add(max(x_char, gene[1]))

ans_sorted = sorted(ans)
print(len(ans_sorted))
print(" ".join(ans_sorted))
