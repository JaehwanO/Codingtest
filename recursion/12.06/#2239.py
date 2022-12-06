graph = list(list(map(int,input())) for _ in range(9))
visited1 = [[False]*9 for _ in range(9)]
visited2 = [[False]*9 for _ in range(9)]
visited3 = [[False]*9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if graph[i][j]:
            visited1[i][graph[i][j]-1] = True
            visited2[j][graph[i][j]-1] = True
            visited3[i//3*3+j//3][graph[i][j]-1] = True

def back(i,j):
    if i == 9:
        for row in graph:
            print(*row,sep="")
        exit(0)

    if graph[i][j]:
        back(i+(j+1)//9,(j+1)%9)
        return
    for k in range(9):
        if visited1[i][k] or visited2[j][k] or visited3[i//3*3+j//3][k]:
            continue
        graph[i][j] = k+1
        visited1[i][k] = visited2[j][k] = visited3[i//3*3+j//3][k] = True
        back(i+(j+1)//9,(j+1)%9)
        graph[i][j] = 0
        visited1[i][k] = visited2[j][k] = visited3[i//3*3+j//3][k] = False

back(0,0)