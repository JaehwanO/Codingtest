ans = []
cnt = 0
for _ in range(3):
    l = list(map(int,input().split()))
    
    for i in l:
        if i ==0:
            cnt+=1
    if cnt == 0:
        ans.append("E")
        cnt = 0
    elif cnt == 1:
        ans.append("A")
        cnt = 0
    elif cnt == 2:
        ans.append("B")
        cnt = 0
    elif cnt == 3:
        ans.append("C")
        cnt = 0
    elif cnt == 4:
        ans.append("D")
        cnt = 0
for i in ans:
    print(i)
