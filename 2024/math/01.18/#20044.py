import sys
n = int(sys.stdin.readline().rstrip())
l = map(int,input().split())
my_list = list(l)
my_list.sort()
answer =[]
for i in range(n):
    answer.append(my_list[i]+my_list[-1-i])
print(min(answer))    