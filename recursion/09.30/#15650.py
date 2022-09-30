# 15650번
n,m = map(int,input().split())
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return #<-다음 라인으로 넘어감
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)

# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# rs = []
# isused = [False]*(n+1)

# def dfs(num):
#     if num == m:
#         print(' '.join(map(str,rs)))
#         return
#     for i in range(num,n+1):
#         if isused[i]==False:
#             isused[i]=True
#             rs.append(i)
#             dfs(num+1)
#             isused[i]=False
#             rs.pop()

# dfs(0)
