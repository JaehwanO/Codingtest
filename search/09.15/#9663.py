import sys

# 대각선의 퀸이 있는지 확인
def check(x):
    for i in range(x):
        if abs(graph[x] - graph[i]) == x - i:
            return False
    return True

# 체스 판의 열을 dfs 탐색
def dfs(queen):
    global res

    # n번째 퀸을 놓으려 한다면 리턴 (n개의 퀸을 놓았기 때문.)
    if queen == n:
        res += 1 # 방법의 수 카운트
        return

    # 모든 체스판의 열을 확인
    for i in range(n):
        # i 번째 열의 퀸을 놓지 않았다면
        if not visited[i]: #if visited = False
            graph[queen] = i # (queen, i)에 퀸을 둔다.

            # 대각선의 겹치는 퀸이 있는지 확인
            if check(queen): #없으면 True
                # 백 트래킹
                visited[i] = True # 퀸을 놓는다.
                dfs(queen + 1) # 재귀적으로 퀸을 놓을 수 있는 열을 찾는다.
                visited[i] = False # 재귀 탐색 후 퀸을 n개 놓을 수 없다면 퀸을 놓지 않는 것으로 초기화 후 다른 열을 탐색

n = int(sys.stdin.readline())
graph = [0 for _ in range(n)] # n번째 열의 퀸의 위치
visited = [False for _ in range(n)] # 체스판의 탐색 여부
res = 0 # 퀸을 놓는 방법의 수

dfs(0)
print(res)