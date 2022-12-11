import sys
T = int(sys.stdin.readline())
for _ in range(T):
    sys.stdin.readline()
    A = []
    count = 0
    r, c = map(int, sys.stdin.readline().split())
    for _ in range(r):
        A.append(sys.stdin.readline())
    for i in range(r):
        for j in range(c-2):
            if A[i][j] == '>' and A[i][j+1] == 'o' and A[i][j+2] == '<':
                count += 1
    for i in range(r-2):
        for j in range(c):
            if A[i][j] == 'v' and A[i+1][j] == 'o' and A[i+2][j] == '^':
                count += 1
    print(count)
    
# t = int(input())
# for _ in range(t):
#     ans = 0
#     candy1 =">o<"
#     candy2 = 'vo^'
#     graph1 = []
#     dumb = input()
#     r,c = map(int,input().split())
#     for _ in range(r):
#         graph1.append(list(input()))

#     graph2 = ([list(i) for i in zip(*graph1)])

#     for i in range(r):
#         tmp = ''.join(graph1[i])
#         if candy1 in tmp:
#             ans += 1

#     for i in range(c):
#         tmp = ''.join(graph2[i])
#         if candy2 in tmp:
#             ans += 1
#     print(ans)