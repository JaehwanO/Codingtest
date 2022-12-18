n = int(input())
order = list(map(int,input().split()))
num = [i for i in range(1,n+1)]
ans = []
for i in range(n):
    ans.insert(order[i],num[i])

print(*ans[::-1])