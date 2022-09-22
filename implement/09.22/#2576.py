l = []
odd = []
for _ in range(7):
    l.append(int(input()))
for i in l:
    if i%2!=0:
        odd.append(i)
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)