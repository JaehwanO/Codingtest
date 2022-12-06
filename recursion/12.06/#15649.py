n,m = map(int,input().split())
visited = [False] * (n+1)
ans = []
def back(i):
    if len(ans) == m:
        print(*ans)
        return
    
    for num in range(1,n+1):
        if visited[num]:
            continue
        ans.append(num)
        visited[num] = True
        back(num+1)
        ans.pop()
        visited[num] = False
        
back(0)