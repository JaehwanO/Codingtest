n, m = map(int,input().split())
l = []
def dfs(s):
    if len(l)==m:
        print(' '.join(map(str,l)))
        return 

    for i in range(1,n+1):
        # if i not in l:
        l.append(i)
        dfs(i+1)
        l.pop()
dfs(1)
