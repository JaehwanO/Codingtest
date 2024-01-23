n,m = map(int,input().split())

basket = [i for i in range(1,n+1)]
tmp = 0
for i in range(m):
    i,j = map(int,input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp
for i in range(n):
    print(basket[i],end='')