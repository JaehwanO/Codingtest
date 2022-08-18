n = int(input())
l = list(map(int,input().split()))
l.sort()
answer = 0
s = sum(l)
for i in range(len(l)):
    # print(l[-i-1])
    answer += s
    s -= l[-i-1]
print(answer)
    
# 1 2 3 3 4 

# 3 1 4 3 2
# 2 5 4 1 3