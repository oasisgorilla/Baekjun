"""2트(일반 위상정렬코드에 heapq사용)"""
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 

def topology_sort():
    result = []
    heap = []

    # 진입차수가 0인 노드를 힙에 넣음
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    
    while heap:
        c = heapq.heappop(heap)
        result.append(c)

        for n in graph[c]:
            indegree[n] -= 1
            if indegree[n] == 0:
                heapq.heappush(heap, n)

    print(' '.join(map(str, result)))


topology_sort()