a_tmp = [0]*26
b_tmp = [0]*26
ans = 0
a = input()
b = input()

for i in a:
    a_tmp[ord(i)-97]+=1
for j in b:
    b_tmp[ord(j)-97]+=1

for i in range(26):
    ans += abs(a_tmp[i]-b_tmp[i])
print(ans)