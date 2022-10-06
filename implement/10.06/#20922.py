N, K = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0

counter = [0] * (max(numbers) + 1)
answer = 0
while right < N:
    if counter[numbers[right]] < K:
        counter[numbers[right]] += 1
        right += 1
    else:
        counter[numbers[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)


# import sys
# input = sys.stdin.readline
# if __name__ == '__main__':
#     n, k = map(int,input().split())
#     l=list(map(int,input().split()))
#     ans = -sys.maxsize
#     for left in range(n):
#         d = {}
#         d[l[left]] = 1
#         right = left + 1
#         while right < n:
#             if l[right] in d:
#                 d[l[right]] += 1
#             else:
#                 d[l[right]] = 1

#             if d[l[right]] > k:
#                 d[l[right]] -= 1
#                 break
#             right += 1
#         ans = max(ans,sum(d.values()))
#         # print(d)
#         # print(sum(d.values()))
#     print(ans)