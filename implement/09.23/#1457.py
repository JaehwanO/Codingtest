n  = int(input())
cnt = [0]*10
for i in str(n):
    cnt[int(i)]+=1

if (cnt[6]+cnt[9])%2==0:
    cnt[6] = (cnt[6]+cnt[9])//2
    cnt[9] = cnt[6]
else:
    cnt[6] = ((cnt[6]+cnt[9])//2)+1
    cnt[9] = cnt[6]

print(max(cnt))