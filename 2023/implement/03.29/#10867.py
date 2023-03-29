n = int(input())
num = set(map(int,input().split()))
num = sorted(list(num))
print(*num)