import sys
import heapq
input = sys.stdin.readline

INF = int(1e9) # 10억

N, M = map(int, input().rstrip().split()) # 헛간 개수, 길의 개수

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start = 1 # 현서의 위치

visited = [False] * (N + 1) # 방문체크

distance = [INF] * (N + 1) # 최단거리

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 최단경로, 노드
    distance[start] = 0 # 시작 노드 최단경로 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드 무시
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            next_dist = dist + cost # 현재 노드를 거쳐 다른 노드로 가는 경우
            # 현재 노드를 거쳐 이동하는 것이 더 짧을 경우
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node)) # 우선순위 큐 삽입

dijkstra(start)

print(distance[N])
