graph = [input() for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result_set = set()
def back(arr,idx,S,Y=0):
    tmp = arr
    if Y>3:
        return
    if idx == 6:
        arr.sort()
        result_set.add((tuple(arr)))
    else:
        adjacents = []
        for node in range(len(arr)):
            for i in range(4):
                nx = arr[node][0] + dx[i]
                ny = arr[node][1] + dy[i]
                if 0<=nx<5 and 0<=ny<5 and (nx,ny) not in arr:
                    adjacents.append((nx,ny))
        for ad in adjacents:
            nx = ad[0]
            ny = ad[1]
            if graph[nx][ny] == "S":
                back(arr+[(nx,ny)],idx+1,S+1,Y)
            else:
                back(arr+[(nx,ny)],idx+1,S,Y+1)

for i in range(5):
    for j in range(5):
        if graph[i][j] == "S":
            back([(i,j)],0,1)

print(len(result_set))