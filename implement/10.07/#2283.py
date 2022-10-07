import sys
if __name__=='__main__':
    input = sys.stdin.readline
    n, k = map(int,input().split())
    dp = [0] * 1000001
    # dp = [0] * 100
    for _ in range(n):
        x,y = map(int,input().split())
        for i in range(x,y):
            dp[i] +=1
    left = 0 
    right = 0
    s = 0
    while True:
        if s < k:
            s += dp[right]
            right += 1
        elif s > k:
            s -= dp[left]
            left += 1
        else: # s == k
            print(left,right)
            break 
        if right == 1000001:
            print("0","0")
            break
    
    # print(dp)
