import sys
n, m = map(int, sys.stdin.readline().split())

numbers = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in sys.stdin.readline().split()]
    numbers.append(nums)

# prefix sum 행렬 만들기

for i in range(1, n + 1):
    for j in range(1, n):
        numbers[i][j + 1] += numbers[i][j]

for j in range(1, n + 1):
    for i in range(1, n):
        numbers[i + 1][j] += numbers[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])
    
    
    # import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0]*n for i in range(n)]
# dp[0][0] = graph[0][0]

# for i in range(0,n):
#     for j in range(0,n):
#         dp[i][j] = dp[i-1][j] + sum(graph[i][:j+1])
# # print(dp)

# for _ in range(m):
#     a1,b1,a2,b2 = map(int,input().split())
# # 1 1 4 4
#     ans = dp[a2-1][b2-1] - dp[a1-2][b2-1] - dp[a2-1][b1-2] + dp[a1-2][b1-2]
#     print(ans)