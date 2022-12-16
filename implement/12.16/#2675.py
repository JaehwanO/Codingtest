t = int(input())
for _ in range(t):
    ans = ''
    n,s = map(str,input().split())
    for i in s:
        ans += i*(int(n))
    print(ans)