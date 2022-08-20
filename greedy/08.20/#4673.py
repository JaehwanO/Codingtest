import sys

target = 10000
d = list(range(1,target+1))
print(d)
l = []
for i in range(1,target):
    temp = sum(map(int, str(i)))
    result = i + int(temp)
    if result <= target:
        l.append(int(result))
        
l.sort()
# print(l)
for j in d:
    if j not in l:
        print(j)