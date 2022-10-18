n = int(input())
u = set()
for _ in range(n):
    u.add(int(input()))

a_b_sum = set()
for i in u:
    for j in u:
        a_b_sum.add(i+j)
ans = {}
for i in u:
    for j in u:
        if (i-j) in a_b_sum:
            ans[i] = (i,j,i-j)
keys = list(ans.keys())
keys.sort(reverse = True)
print(keys[0])