d = ["a", "e", "i", "o", "u"]
s = input()
cnt = 0 
for i in s:
    if i in d:
        cnt += 1
print(cnt)