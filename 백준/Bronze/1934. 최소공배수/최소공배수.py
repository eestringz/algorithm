def GCD(x, y):
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    gcd = GCD(a, b)
    lcm = a * b // gcd
    print(lcm)