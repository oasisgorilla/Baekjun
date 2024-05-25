from collections import deque
import sys
input = sys.stdin.readline


def BFS(start, group):
    que = deque([start])
    visited[start] = group # 함수 바깥의 visited는 노드 방문여부, 여기는 같은 그룹여부를 체크한다.

    while que: # 큐가 빌 때까지 반복
        node = que.popleft() # 현재 탐색 중인 노드 포인터

        for link_node in graph[node]: # link_node는 neighbor 랑 같은 의미이다.
            if not visited[link_node]: # 방문여부 확인
                que.append(link_node) # 방문하지 않은 노드는 큐로 보낸다.
                visited[link_node] = -visited[node] # visited[이웃노드] = -1 >> visited가 1인 그룹과 -1인 그룹으로 나눔
            elif visited[link_node] == visited[node]: # 현재 탐색중인 노드의 이웃 노드가 현재 탐색 중인 노드와 같은 그룹이면
                return True

    return False


if __name__ == "__main__":
    K = int(input())

    for _ in range(K):
        V, E = map(int, input().split())

        graph = [[] for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (V+1)

        for i in range(1, V+1):
            if not visited[i]: # 방문 여부가 F이면
                result = BFS(i, 1) # BFS를 돌린다. 만약 이분그래프가 아니면 True를 내보낸다.
                if result: # True를 받으면 NO를 출력
                    print("NO")
                    break
        else:
            print("YES")