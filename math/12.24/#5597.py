n = [False]*(31)
for _ in range(28):
    n[int(input())] = True

for i,v in enumerate(n[1:]):
    if not v:
        print(i+1)
