import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E, P = map(int, input().rstrip().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [False] * (V + 1)
distance = [INF] * (V + 1)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start)) # 출발지점까지 거리 삽입
    distance[start] = 0 # 출발지점 최단경로 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 최단거리가 나온 노드는 무시
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            next_dist = dist + cost

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(q, (next_dist, next_node))

    return distance[end]

route1 = dijkstra(1, V)
route2 = dijkstra(1, P) + dijkstra(P, V)

if route1 == route2:
    print("SAVE HIM")
else:
    print("GOOD BYE")

