n, m = map(int,input().split())
basket = ['0']*(n+1)
for _ in range(m):
    i,j,k = map(int,input().split())
    for t in range(i,j+1):
        basket[t] = str(k)

print(' '.join(basket[1:]))