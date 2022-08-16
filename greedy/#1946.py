import sys
t = int(sys.stdin.readline())
for i in range(t):
    cnt = 1
    nList = []
    
    n = int(sys.stdin.readline())
    for _ in range(n):
        nList.append(list(map(int, sys.stdin.readline().split())))

    nList.sort()
    mx = nList[0][1]
    # print(nList)
    # print(mx)
    for j in range(1, n):
        if mx > nList[j][1]:
            cnt += 1
            mx = nList[j][1]

    print(cnt)