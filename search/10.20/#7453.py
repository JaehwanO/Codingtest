import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
left = []
right = {}
for i in range(n):
    for j in range(n):
        left.append(A[i]+B[j])
        right[C[i]+D[j]] = right.get(C[i]+D[j], 0) + 1
        
count = 0
for i in left:
    count += right.get(-i, 0)
    
print(count)

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# n = int(input())
# A, B, C, D = [], [], [], []
# for i in range(n):
#     a, b, c, d = map(int, input().split())
#     A.append(a)
#     B.append(b)
#     C.append(c)
#     D.append(d)
    
# left = []
# right = defaultdict(int)
# for i in range(n):
#     for j in range(n):
#         left.append(A[i]+B[j])
#         right[C[i]+D[j]] += 1
        
# count = 0
# for i in left:
#     count += right[-i]
    
# print(count)