import sys
input = sys.stdin.readline
N  = int(input())
index = 665
l = []
cnt = 0 
while True:
    index += 1
    l = list(str(index))
    for i in range(len(l)-2):
        if l[i] == '6' and l[i+1] == '6' and l[i+2] == '6':
            cnt +=1
            break
    if cnt == N:
        print(index)
        break

























# N = int(input())

# index = 665
# count = 0

# while True:
#     index += 1
#     number = index

#     n_list = list(map(int,str(number)))
#     # print(n_list)
#     for i in range(len(n_list)-2):
#         if n_list[i] == 6 and n_list[i+1] == 6 and n_list[i+2] == 6:
#             count += 1
#             break

#     if N == count:
#         print(index)
#         break