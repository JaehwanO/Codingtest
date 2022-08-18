n = int(input())
tip = 0
tips = []
for i in range(n):
    t = int(input())
    tips.append(t)
tips.sort(reverse=True)
for j in range(n):
    if tips[j] - j < 0:
        continue
    tip += (tips[j]-j)
print(tip)