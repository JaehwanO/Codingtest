from itertools import permutations #순열 함수

N = int(input())
N_list = [i for i in range(1, N+1)]

for numbers in list(permutations(N_list)):
    for num in numbers:
        print(num, end=' ')
    print()

# import sys
# import itertools

# n = int(sys.stdin.readline())
# l = list(i for i in range(1,n+1))
# p = list(itertools.permutations(l,n))
# for i in p:
#     print (i,end=' ')
#     print()