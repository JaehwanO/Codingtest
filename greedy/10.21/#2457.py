import sys

n = int(input())
info = [] 
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    info.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

info = sorted(info, key = lambda x : (x[0],x[1]))
# print(info)
cnt = 0 
end = 0
target = 301

while info:
    if target >= 1201 or target < info[0][0]:
        break
    
    for _ in range(len(info)):
        if target >= info[0][0]:
            if end <= info[0][1]:
                end = info[0][1]
            info.remove(info[0])
        else:
            break
    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
