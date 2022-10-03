n, k = map(int,input().split())
d= [[0]* i for i in range(1,n+2)]

d[0][0] = 1
d[1][0] = 1
d[1][1] = 1
# print(d[2][0])

for i in range(2,n+1):
    for j in range(0,i+1):
        if j == 0:
            d[i][j] = 1
        if j == i:
            d[i][j] = 1
        if j!=0 and j!=i:
            d[i][j] = d[i-1][j-1]+d[i-1][j]
            
print(d[n][k]%10007)