n,m = map(int,input().split())
a = [i for i in range (1,n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    tmp = a[i-1:j]
    tmp.reverse()
    a[i-1:j] = tmp

for i in range(n):
    print(a[i],end=' ')
