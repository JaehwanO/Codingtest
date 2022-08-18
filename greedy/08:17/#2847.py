import sys
n = int(sys.stdin.readline())
l = []
count = 0

for i in range(n):
    l.append(int(input()))

count = 0
for i in range(n-2, -1, -1):
    if l[i] >= l[i+1]:
        count += l[i] - l[i+1] + 1
        l[i] = l[i+1]-1

print(count)