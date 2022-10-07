import sys
input = sys.stdin.readline
A, B = map(int, input().split())

state = [True] * (int(B**0.5)+1)
state[1] = False
for i in range(2, int(B ** 0.5)+1):
    if i * i > int(B ** 0.5):
        break
    if not state[i]:
        continue
    for j in range(i*i, int(B ** 0.5)+1, i):
        state[j] = False
cnt = 0
for i in range(1, len(state)):
    if state[i]:
        j = i * i
        while True:
            if j < A:
                j *= i
                continue
            if j > B:
                break
            j *= i
            cnt += 1

print(cnt)