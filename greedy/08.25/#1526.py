n = int(input())
answer = 0
for i in range(3,n+1):
    minsu = []
    for j in str(i):
        if j =='4' or j == '7':
            minsu.append(1)
        else:
            minsu.append(0)
    if 0 in minsu:
        # print("not")
        pass
    else:
        answer = max(i,answer)
        # print(max(i,answer))
print(answer)