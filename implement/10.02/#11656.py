from re import L


n = input()[::-1]
s = ''
l = []
for i in n:
    s+= i
    l.append(s[::-1])
l.sort()
# print(l)
for i in l:
    print(i)