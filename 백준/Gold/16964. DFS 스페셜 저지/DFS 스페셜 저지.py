import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
graph = [[] for _ in range(N + 1)]

# 그래프 입력
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서 입력
seq = list(map(int, input().split()))

# BFS로 부모 관계 구하기
def bfs_to_find_parents():
    parent = [0] * (N + 1)  # 각 노드의 부모 저장
    visited = [False] * (N + 1)
    queue = deque([1])  # 루트 노드는 1
    visited[1] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
    
    return parent

# DFS 방문 순서 유효성 확인
def is_valid_dfs_order():
    parent = bfs_to_find_parents()
    position = [0] * (N + 1)  # 각 노드의 방문 순서 저장
    for i, node in enumerate(seq):
        position[node] = i

    # 각 노드의 자식 노드를 입력 순서에 맞게 정렬
    for i in range(1, N + 1):
        graph[i].sort(key=lambda x: position[x])

    # DFS로 순서 확인
    stack = [1]  # 루트에서 시작
    visited = [False] * (N + 1)
    visited[1] = True
    idx = 0

    while stack:
        current = stack.pop()
        if seq[idx] != current:  # 순서가 맞지 않으면 잘못된 입력
            return 0
        idx += 1

        for neighbor in reversed(graph[current]):  # 스택을 사용하므로 뒤에서부터 확인
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return 1

# 결과 출력
print(is_valid_dfs_order())
