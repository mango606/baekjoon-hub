import sys
sys.setrecursionlimit(10**6)  # 파이썬 기본 재귀 한도를 늘림

class Node:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None
    root = nodes.pop(0)
    root_node = Node(root[0], root[1], root[2])
    left_nodes = [node for node in nodes if node[1] < root_node.x]
    right_nodes = [node for node in nodes if node[1] > root_node.x]
    root_node.left = build_tree(left_nodes)
    root_node.right = build_tree(right_nodes)
    return root_node

def preorder_traversal(node, result):
    if node:
        result.append(node.data)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)

def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.data)

def solution(nodeinfo):
    nodes_with_info = [(i+1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    sorted_nodes = sorted(nodes_with_info, key=lambda x: (-x[2], x[1]))
    
    root = build_tree(sorted_nodes)
    
    preorder_result, postorder_result = [], []
    preorder_traversal(root, preorder_result)
    postorder_traversal(root, postorder_result)
    
    return [preorder_result, postorder_result]