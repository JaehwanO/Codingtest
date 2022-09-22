l = []
for _ in range(9):
    l.append(int(input()))
print(max(l))
print(l.index(max(l))+1)