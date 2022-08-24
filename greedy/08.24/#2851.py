l = []
for _ in range(10):
    l.append(int(input()))
compare = [0]
s = 0
for i in l:
    s += i
    if s <= 100:
        compare[0] = max(compare[0],s)
    else:
        compare.append(s)
        break
# print(compare)
if abs(100-compare[0]) < abs(100-compare[1]):
    print(compare[0])
else:
    print(compare[1])