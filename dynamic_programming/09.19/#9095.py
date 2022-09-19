#D4 = D1 + D2 + D3
T = int(input())
d = [0] * 100
for _ in range(T):
    n = int(input())
    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4,n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[n])