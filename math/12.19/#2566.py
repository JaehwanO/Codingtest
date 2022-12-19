graph = [list(map(int,input().split())) for _ in range(9)]
# print(graph)
max_num = 0
for i in graph:
    max_num= max(max_num,max(i))
print(max_num)

for i in range(9):
    for j in range(9):
        if graph[i][j] == max_num:
            print(i+1,j+1)