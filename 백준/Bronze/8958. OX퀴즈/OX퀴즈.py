N = int(input())

for i in range(N):
    arr=list(input())
    score = 0
    sum = 0
    for j in arr:
        if j == 'O':
            score +=1
        else:
            score = 0
        sum += score
    print(sum)