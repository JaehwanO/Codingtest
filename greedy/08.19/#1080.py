def change(r,c):
    for i in range(3):
        for j in range(3):
            if a[r+i][c+j]==1:
                a[r+i][c+j]=0
            else:
                a[r+i][c+j]=1




n,m=map(int,input().split())
a=[list(map(int,input()))for _ in range(n)]
b=[list(map(int,input()))for _ in range(n)]

print(a)
count=0
for i in range(0,n-2):
    for j in range(0,m-2):
        if a[i][j]!=b[i][j]:
            change(i,j)
            count+=1


for i in range(n):
    for j in range(m):
        if a[i][j]!=b[i][j]:
            print(-1)
            exit()

print(count)