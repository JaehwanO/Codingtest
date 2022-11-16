t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    dp = [[0]*(n+1) for _ in range(k+1)]
    zero = [i for i in range(1,n+1)]

    for i in range(k):
        for j in range(1,n):
            zero[j] += zero[j-1]
    print(zero[n-1])