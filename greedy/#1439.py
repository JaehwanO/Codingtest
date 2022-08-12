# s = str(input())
# my = list(s)
# count = 0

# for i in range(len(my)-1):
#     if my[i]!=my[i+1]:
#         count += 1
# if count%2 !=0 and count//2 > 1:
#     print(count//2 + 1)
# elif count%2 ==0 and count//2 > 1:
#     print(count//2)
# else:
#     print(count)
    
s = input()

cnt = 0
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cnt += 1
print((cnt+1)//2)