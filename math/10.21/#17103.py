import sys
input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]
m = max(nums)

prime = [False,False] + [True] * (m-1)
for i in range(2,int(m**(0.5)+1)):
    if prime[i]:
        for j in range(i+i,m+1,i):
            if prime[j]:
                prime[j] = False

for num in nums:
    cnt = 0
    for i in range((num//2)+1):
        if prime[i] and prime[num-i]:
            cnt += 1
    print(cnt)