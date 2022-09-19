import sys
input = sys.stdin.readline
# 초콜릿 먹는 개수
k = int(input())
# 1,2,4,8,16 .. 초콜릿 크기(정사각형의 개수)를 정하기 위한 변수
size = 1
# 잘라야 하는 횟수 카운트
count = 0
while size < k:
    size = size << 1
    
result1 = size

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1

print(result1, count)

# n = int(input())
# s = [2**i for i in range (n+1)]
# choco = 0
# for i in s:
#     if i>n:
#         choco = max(i,choco)
#         break
# # print(choco)

# diff = choco-n
# cnt = 0 
# c = choco
# while True:
#     cnt += 1
#     if choco <= diff:
#         cnt -= 1
#         break
#     choco = (choco/2)%17859

# print(c, cnt)
