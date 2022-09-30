import sys
I = sys.stdin.readline
P = sys.stdout.write

T = int(I())
A = []
for _ in range(T):
    A.append(int(I()))

A.sort()
P('\n'.join(map(str, A)))