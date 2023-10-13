L = int(input())
N = int(input())
cake = [0] * L
expect = []
real = [0] * L
for i in range(1, N + 1):
    P, K = map(int, input().split())
    expect.append(K - P)
    for j in range(P - 1, K):
        if cake[j] == 0:
            cake[j] = i

for i in range(L):
    if cake[i] == 0: continue
    real[cake[i]] += 1

print(expect.index(max(expect)) + 1)
print(real.index(max(real)))