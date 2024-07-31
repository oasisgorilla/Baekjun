import sys
import heapq

input = sys.stdin.readline
max_int = sys.maxsize

V, E = map(int, input().split()) # V: node, E : link

start = int(input().rstrip()) # start node, starting from 1

graph = [[] for _ in range(V + 1)] # 인접그래프, adjust the index to start node

for _ in range(E):
    u, v, w = map(int, input().split()) # u : from, v : to, w : weight
    graph[u].append((v, w)) # make 인접그래프

result = [max_int for _ in range(V + 1)]
result[start] = 0

priority_q = []
heapq.heappush(priority_q, (0, start)) # distance, node

while priority_q:
    cur_dist, cur_node = heapq.heappop(priority_q)

    if cur_dist > result[cur_node]: # 현재 보고 있는 거리가 최소가아닐 경우 갱신하지 않음
        continue

    for neighbor, weight in graph[cur_node]: # 현재 보고 있는 노드와 인접한 노드 확인
        dist = cur_dist + weight

        if dist < result[neighbor]: # 현재 보고 있는 노드에서 이웃으로 가는 거리가 더 작으면 갱신
            result[neighbor] = dist
            heapq.heappush(priority_q, (dist, neighbor)) # 이웃의 이웃노드 거리 확인을 위해 힙에 추가

for i in range(1, V + 1):
    if result[i] == max_int:
        print("INF")
    else:
        print(result[i])