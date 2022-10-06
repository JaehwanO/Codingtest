import sys

n, d, k, c = map(int, sys.stdin.readline().rsplit())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lp, rp = 0, 0
answer = 0

while lp != n:
    rp = lp + k
    case = set() # Reset casep
    addable = True
    for i in range(lp, rp):
        i %= n # Rotating
        case.add(arr[i])
        if arr[i] == c: 
            addable = False

    cnt = len(case)
    if addable: 
        cnt += 1
    answer = max(answer, cnt)
    lp += 1

print(answer)

# import sys
# input = sys.stdin.readline

# if __name__ == '__main__':
#     n,d,k,c = map(int,input().split())
#     l = []
#     total = []
#     for _ in range (n):
#         l.append(int(input()))
#     # print(l)

#     for left in range(n):
#         right = left + 1
#         sushi = [l[left]]
#         # print(sushi)

#         while len(sushi) < k:
#             if right >= n:
#                 right = right - n
            
#             if l[left] != l[right]:
#                 sushi.append(l[right])
#                 right += 1

#             elif l[left] == l[right]:
#                 break

#         if len(sushi) == k:
#             total.append(sushi)

#     # print(total)
#     m = -(sys.maxsize)
#     for i in total:
#         i = set(i)
#         # print(i)
#         if c not in i:
#             m = max(m,len(i)+1)
 
#         else:
#             m = max(m,len(i))
#     print(m)