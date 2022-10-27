import sys
import copy
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())


#위 동서남북 아래
dice = [0,0,0,0,0,0]
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

order = list(map(int,input().split()))
# print(graph)
# print(order)
for i in range(k):
    if order[i] == 1:
        x = x
        y = y+1
        if 0<=x<n and 0<=y<m:
            tmp = dice.copy()
            # 위 = 서, 동 = 위, 아래 = 동,서 = 아래
            dice[0] = tmp[2]
            dice[1] = tmp[0]
            dice[5] = tmp[1]
            dice[2] = tmp[5]
            if graph[x][y] ==0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
            print(dice[0])
        else:
            x = x
            y = y - 1


    elif order[i] == 2:
        x = x
        y = y-1
        if 0<=x<n and 0<=y<m:
            tmp = dice.copy()
            # 위 = 동, 서 = 위, 아래 = 서, 동 = 아래
            dice[2] = tmp[0]
            dice[0] = tmp[1]
            dice[1] = tmp[5]
            dice[5] = tmp[2]
            if graph[x][y] ==0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
            print(dice[0])
        else:
            x = x
            y = y + 1
        
    elif order[i] == 3:
        x = x-1
        y = y
        if 0<=x<n and 0<=y<m:
            tmp = dice.copy()
            # 북 = 위 , 아래 = 북, 남 = 아래, 위 = 남
            dice[4] = tmp[0]
            dice[5] = tmp[4]
            dice[3] = tmp[5]
            dice[0] = tmp[3]  
            if graph[x][y] == 0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
            print(dice[0])
        else:
            x = x + 1
            y = y

    elif order[i] == 4:
        x = x+1
        y = y
        if 0<=x<n and 0<=y<m:
            tmp = dice.copy()
            # 북 = 위 , 아래 = 북, 남 = 아래, 위 = 남
            dice[0] = tmp[4]
            dice[4] = tmp[5]
            dice[5] = tmp[3]
            dice[3] = tmp[0]
            if graph[x][y] == 0:
                graph[x][y] = dice[5]
            else:
                dice[5] = graph[x][y]
                graph[x][y] = 0
            print(dice[0])
        else:
            x = x -1
            y = y