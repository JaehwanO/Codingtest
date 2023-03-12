scores = []
for _ in range(8):
    scores.append(int(input()))

top_five = sorted(scores,reverse=True)[:5]
ans = []
for num in top_five:
    ans.append(scores.index(num)+1)
ans.sort()
print(sum(top_five))
print(*ans)