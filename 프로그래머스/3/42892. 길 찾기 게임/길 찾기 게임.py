from sys import setrecursionlimit
setrecursionlimit(10**4) # 재귀 호출 한도 늘림

def solution(nodeinfo):
    nodes = sorted([(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[1], x[0]))
    preorder_list, postorder_list = [], []

    def dfs(nodes):
        if not nodes:
            return
        root = nodes[0] # 노드 선택
        preorder_list.append(root[2])  # 전위 순회: 루트 방문 후 좌우 서브트리 순회

        # 루트 노드를 기준으로 좌우 서브트리 분할
        left_subtree = [node for node in nodes if node[0] < root[0]]
        right_subtree = [node for node in nodes if node[0] > root[0]]

        # 좌우 서브트리에 대해 재귀적으로 dfs 호출
        dfs(left_subtree)
        dfs(right_subtree)
        postorder_list.append(root[2])  # 후위 순회: 좌우 서브트리 순회 후 루트 방문

    dfs(nodes)
    print(nodes)
    return [preorder_list, postorder_list]