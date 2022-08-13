import sys
n = int(sys.stdin.readline().rstrip())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))
l.sort()
answer = 0 
for i in range(n):
    answer += abs((i+1)-l[i])
print(answer)