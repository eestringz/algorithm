n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    summ = 0
    for r in range(i,x+1):
        for c in range(j,y+1):
            summ += arr[r-1][c-1]
    print(summ)