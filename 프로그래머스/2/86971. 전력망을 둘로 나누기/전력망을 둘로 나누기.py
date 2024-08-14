from collections import deque

def solution(n, wires):
    def bfs(graph, start, n):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        count = 0

        while queue:
            cur = queue.popleft()
            count += 1

            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return count
    
    answer = 100
    graph = [[] for _ in range(n + 1)]

    # 인접그래프 만들기
    for node1, node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)

    # 그래프 간선 자른 모든 경우 계산
    for node1, node2 in wires:
        graph[node1].remove(node2)
        graph[node2].remove(node1)

        group_size = bfs(graph, node1, n)

        # 두 그룹의 차이 계산
        rest_group_size = n - group_size
        chai = abs(group_size - rest_group_size)
        answer = min(answer, chai)

        graph[node1].append(node2)
        graph[node2].append(node1)

    return answer