n,m = map(int,input().split())
bag = [0]*n(+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    for n in range(a,b+1):
        bag[n]=c

for i in range(1,n+1):
    print(bag[i],end= ' ')


