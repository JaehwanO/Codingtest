import sys
input=sys.stdin.readline
n=int(input())
#n일까지 벌 수 있는 최대수익을 저장,
d=[0]*20
tplist=[[0,0]]
for _ in range(n):
  t,p=map(int,input().split())
  tplist.append([t,p])
# print(tplist)
for i in range(1,n+1):
  x=tplist[i][0]-1
  d[i]=max(d[i-1],d[i])
  d[i+x] = max(d[i-1]+tplist[i][1],d[i+x])
  
print(d[n])

# # 퇴사 DP 
# n = int(input())
# T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]
# for i in range(n):
#     a,b = map(int, input().split())
#     T[i] = a
#     P[i] = b

# # dp[i]는 i번째날까지 일을 했을 때, 최대값이다. 
# dp =[0 for i in range(n+1)]

# for i in range(len(T)-2, -1, -1):      # 역순으로 진행
#     if T[i]+i <= n:       # 날짜를 초과하지 않을 경우.
#         dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])   
#     else:                 # 날짜를 초과할 경우.
#         dp[i] = dp[i+1]
# print(dp[0])