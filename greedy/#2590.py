paper = [0]
ans = 0
for _ in range(6):
    paper.append(int(input()))

if paper[6]:
    ans += paper[6]

while paper[5]:
    area = 36 - 5*5
    paper[5] -= 1
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[4]:
    area = 36 - 4*4
    area -= min(paper[2], 5) * 4
    paper[4] -= 1
    paper[2] = max(paper[2]-5, 0)
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[3]:
    area = 36 - 9 * min(paper[3], 4)
    if paper[3] >= 4:
        paper[3] -= 4
        area = 0
    elif paper[3] == 3:
        area -= min(1, paper[2]) * 4
        paper[3] -= 3
        paper[2] = max(paper[2]-1, 0)
    elif paper[3] == 2:
        area -= min(3, paper[2]) * 4
        paper[3] -= 2
        paper[2] = max(paper[2]-3, 0)
    else:
        area -= min(5, paper[2]) * 4
        paper[3] -= 1
        paper[2] = max(paper[2]-5, 0)

    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[2]:
    area = 36 - 4 * min(paper[2], 9)
    paper[2] = max(paper[2]-9, 0)
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[1]:
    paper[1] = max(paper[1]-36, 0)
    ans += 1

print(ans)