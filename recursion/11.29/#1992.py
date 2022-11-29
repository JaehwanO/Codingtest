n = int(input())
board = list(list(map(int,input())) for _ in range(n))

def dfs(x,y,n):
    check_num = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != check_num:
                check_num = -1
                break

    if check_num == -1:
        print("(",end='')
        n = n//2
        dfs(x,y,n)
        dfs(x,y+n,n)
        dfs(x+n,y,n)
        dfs(x+n,y+n,n)
        print(")",end='')
    
    elif check_num == 1:
        print(1,end='')
    elif check_num == 0:
        print(0,end='')

dfs(0,0,n)
