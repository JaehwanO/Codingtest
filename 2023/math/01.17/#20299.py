import sys
input = sys.stdin.readline

N, S, M =map(int, input().split())
answer=[]
count=0
for i in range(N):
    team = list(map(int, input().split()))
  
    isPass = True
    for i in team:
        if i < M:
            isPass = False
            break
    if isPass:
        if sum(team) >= S:
            answer.extend(team)
            count += 1
print(count)
print(*answer)