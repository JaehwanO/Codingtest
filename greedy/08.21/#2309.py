n = 9
temp1, temp2 = 0, 0
arr = [int(input()) for _ in range(n)]
 
for i in range(n):
    for j in range(i+1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            temp1 = arr[i]
            temp2 = arr[j]
 
arr.remove(temp1)
arr.remove(temp2)
 
print('\n'.join(map(str, sorted(arr))))


# n = 9
# l = []
# for _ in range(n):
#     l.append(int(input()))
# l.sort()
# s = sum(l)
# answer = 0
# not_nanjang =[]
# for i in range(n-1):
#     for j in range(i+1,n):
#         answer = s - l[i] - l[j]
#         if answer == 100:
#             not_nanjang.append(l[i])
#             not_nanjang.append(l[j])
#             break
#         break
# print(not_nanjang)
# for k in l:
#     if k not in not_nanjang:
#         print(k)