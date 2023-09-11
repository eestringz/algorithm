import math

M, N = map(int, input().split())

prime = [0] * 2 + [1] * (N - 1)
for i in range(2, int(math.sqrt(N + 1)) + 1):
    if prime[i] == 1:
        for j in range(2 * i, N + 1, i):
            prime[j] = 0

lst = [i for i in range(M, N + 1) if prime[i] == 1]
print(*lst, sep='\n')