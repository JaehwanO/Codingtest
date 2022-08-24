a, b, c, n = map(int, input().split())
flag = False

for i in range(0, n+1, a): # a배수만큼 증가
    for j in range(0, n+1, b): # b배수만큼 증가
        for k in range(0, n+1-i-j, c): # c배수만큼 증가
            if i+j+k == n:
                flag = True
# 방에 할당된 인원의 수 (i+j+k)가 n과 같으면 true
if flag == True:
    print(1)
else:
    print(0)