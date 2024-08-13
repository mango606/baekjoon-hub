def solution():
    n = int(input())  # 명제의 수
    graph = [[False] * 26 for _ in range(26)]  # 26개 문자에 대한 그래프
    
    for _ in range(n):
        a, _, b = input().split()
        graph[ord(a) - ord('a')][ord(b) - ord('a')] = True

    for i in range(26):
        graph[i][i] = True

    for k in range(26):
        for i in range(26):
            for j in range(26):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    m = int(input())  # 질문의 수
    result = []
    for _ in range(m):
        a, _, b = input().split()
        if graph[ord(a) - ord('a')][ord(b) - ord('a')]:
            result.append("T")
        else:
            result.append("F")
    
    for res in result:
        print(res)

if __name__ == "__main__":
    solution()