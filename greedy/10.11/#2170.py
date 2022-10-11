import sys
input = sys.stdin.readline
n = int(input())
line = []
for _ in range (n):
    x,y = map(int,input().split())
    line.append((x,y))
line = sorted(line, key = lambda x: (x[0],x[1]))
# print(line)
start = line[0][0]
end = line[0][1]
ans = 0

for i in range(1, n):
    if end >= line[i][1]:
        continue
    
    elif line[i][0] <= end < line[i][1]:
        end = line[i][1]
    
    elif end < line[i][0]:
        ans += end - start
        start = line[i][0]
        end = line[i][1]

ans += end - start
print(ans)