l = [i for i in range(1,21)]

for _ in range(10):
    a,b = map(int,input().split())
    temp = l[a-1:b]
    temp.reverse()
    l[a-1:b] = temp

# print(l)
for i in l:
    print(i, end= " ")