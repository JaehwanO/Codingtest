import sys
input = sys.stdin.readline

n, m = map(int,input().split())
rs = []
isused = [False]*(n+1)

def dfs(num):
    if num == m:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,n+1):
        if isused[i]==False:
            isused[i]=True
            rs.append(i)
            dfs(num+1)
            isused[i]=False
            rs.pop()

dfs(0)