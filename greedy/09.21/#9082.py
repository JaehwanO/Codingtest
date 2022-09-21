from re import I, L


T = int(input())
dx =[1,0,-1]
for _ in range(T):
    ans = 0
    n = int(input())
    info = list(map(int,input()))
    mine = list(input())
    print(info)
    # print(mine)
    new_info = []

    for i in range(n-1):
        x = i
        cnt = 0


        mine[i] = "*"
        for j in range(3):
            nx = x + dx[j]
            if 0<=nx<n and mine[nx] == "*":
                cnt +=1
        if cnt <= info[i] or abs(info[i]-info[i+1])<1:
            mine[i] = "*"
        if cnt > info[i] and abs(info[i]-info[i+1])>=1:
            mine[i] = "#"
        if cnt > info[i] and abs(info[i]-info[i+1])==0:
            mine[i] = "#"
        print(mine)
        