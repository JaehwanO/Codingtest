import sys

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline


def dfs(x):
    global ans
    vis[x] = True
    cycle.append(x)
    num = arr[x]

    if vis[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    vis = [False] * (n + 1)
    ans = []

    for i in range(1, n + 1):
        if not vis[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))
    

# import sys
# from collections import deque
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 7)
# t = int(input())


# def bfs(a):
#     q = deque()
#     selected = []
#     a,b = students[a][0],students[a][1]
#     q.append((a,b))
#     if a==b:
#         visited[a] = True
#     else:
#         while q:
#             x,y = q.popleft()
#             selected.append(x)
#             na,nb = students[y][0], students[y][1]
#             if x == na and y == nb:
#                 continue
#             if na == selected[0]:
#                 for i in selected:
#                     visited[i] = True
#             else:
#                 q.append((na,nb))

# for _ in range(t):
#     n = int(input())
#     tmp = [0] + list(map(int,input().split()))
#     students = []
#     ans = 0
#     visited = [False] * (n+1)

#     for i in range(0,n+1):
#         students.append([i,tmp[i]])

#     for i in range(1,n+1):
#         if not visited[i]:
#             bfs(i)
#     s = visited.count(False)
#     print(s-1)