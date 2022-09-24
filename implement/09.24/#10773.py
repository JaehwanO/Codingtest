k = int(input())
l = []

for _ in range(k):
    l.append(int(input()))
    if l[-1] == 0:
        l.pop()
        l.pop()
print(sum(l))