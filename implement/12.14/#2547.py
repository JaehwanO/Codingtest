t = int(input())
for _ in range(t):
    input()
    n = int(input())
    candy = [int(input()) for _ in range(n)]
    print("YES" if sum(candy)%len(candy) == 0 else "NO")
