n, k = map(int, input().split())

s = list(input().rstrip())
count = 0
for i in range(len(s)):
    if s[i] == "P":
        for j in range (i-k,i+k+1):
            if 0 <= j < n and s[j] == "H":
                count +=1
                s[j] = "taken"
                break
print(count)