# 정답코드
import sys
n, k = map(int, sys.stdin.readline().split())
nums = [] # 나열한 수
erase = [] # 지운 수
for i in range(2, n+1):
    nums.append(i)
    
while len(nums) > 0:
    p = nums[0] # 가장 작은 수 p
    temp = []
    for i in range(len(nums)):
        if nums[i] % p == 0: # p의 배수를 erase 리스트에 넣음
            erase.append(nums[i])
        else:
            temp.append(nums[i]) # 남아있는 숫자(p의 배수가 아닌 수)
    nums = temp
print(erase[k-1])