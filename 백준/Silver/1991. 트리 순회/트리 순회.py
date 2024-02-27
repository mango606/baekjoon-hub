class Node:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node

def preorder(node):
    print(node.data, end='') # 루트
    if node.left != '.': preorder(tree[node.left]) # 왼쪽 자식
    if node.right != '.': preorder(tree[node.right]) # 오른쪽 자식

def inorder(node):
    if node.left != '.': inorder(tree[node.left]) # 왼쪽 자식
    print(node.data, end='') # 루트
    if node.right != '.': inorder(tree[node.right]) # 오른쪽 자식

def postorder(node):
    if node.left != '.': postorder(tree[node.left]) # 왼쪽 자식
    if node.right != '.': postorder(tree[node.right]) # 오른쪽 자식
    print(node.data, end='') # 루트

n = int(input()) # 노드의 개수
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = Node(root, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])