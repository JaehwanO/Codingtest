import sys
input = sys.stdin.readline
n = int(input().rstrip())
tree = {}

for _ in range(n):
    root,left,right = map(str,input().split())
    tree[root] = [left,right]

def preorder(node):
    if node != '.':
        print(node,end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node,end='')
        inorder(tree[node][1])
         
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end='')

preorder("A")
print()
inorder("A")
print()
postorder("A")

# import sys
 
# N = int(sys.stdin.readline().strip())
# tree = {}
 
# for n in range(N):
#     root, left, right = sys.stdin.readline().strip().split()
#     tree[root] = [left, right]
 
 
# def preorder(root):
#     if root != '.':
#         print(root, end='')  # root
#         preorder(tree[root][0])  # left
#         preorder(tree[root][1])  # right
 
 
# def inorder(root):
#     if root != '.':
#         inorder(tree[root][0])  # left
#         print(root, end='')  # root
#         inorder(tree[root][1])  # right
 
 
# def postorder(root):
#     if root != '.':
#         postorder(tree[root][0])  # left
#         postorder(tree[root][1])  # right
#         print(root, end='')  # root
 
 
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')
