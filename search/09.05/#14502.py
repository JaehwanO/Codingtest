import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

arr=[]
answer=[]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(N):
    arr.append(list(map(int,input().split())))