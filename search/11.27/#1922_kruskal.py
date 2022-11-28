n = int(input())
m = int(input())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



edges = []
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

result = 0

for edge in edges:
    cost,a,b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)


# n = int(input())
# m = int(input())
# edges=[]
# parent =[0] * (n+1)

# def find_parent(parent,x):
#     if parent[x]!=x:
#         parent[x] = find_parent(parent,parent[x])
#     return parent[x]

# def union_parent(parent,a,b):
#     a = find_parent(parent,a)
#     b = find_parent(parent,b)
#     if a<b:
#         parent[b] = a
#     else:
#         parent[a] = b


# for i in range(1,n+1):
#     parent[i] = i


# for _ in range(m):
#     a,b,c = map(int,input().split())
#     edges.append((c,a,b))

# edges.sort()

# result = 0
# for edge in edges:
#     cost,a,b = edge

#     if find_parent(parent,a) != find_parent(parent,b):
#         union_parent(parent,a,b)
#         result += cost

# print(result)