import sys
input=sys.stdin.readline

tc=int(input())

dp=[[0 for _ in range(3)] for i in range(100001)]

dp[1]=[1,0,0]
dp[2]=[0,1,0]
dp[3]=[1,1,1]

for i in range(4,100001):
    # 6일때 만약

    # 5에서 2와 3으로 끝난거에 1 붙이기
    dp[i][0]=dp[i-1][1]%1000000009+dp[i-1][2]%1000000009
    # 4에서 1과 3으로 끝난거에 2붙이기
    dp[i][1]=dp[i-2][0]%1000000009+dp[i-2][2]%1000000009
    # 3에서 1과 2로 끝난거에 3붙이기
    dp[i][2]=dp[i-3][0]%1000000009+dp[i-3][1]%1000000009

for i in range(tc):
    n=int(input())
    print(sum(dp[n]) % 1000000009)