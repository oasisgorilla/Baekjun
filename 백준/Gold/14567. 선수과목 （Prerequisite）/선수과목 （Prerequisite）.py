import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# topology
def topology_sort():
    semesters = [0] * (N + 1)
    q = deque([])
    
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            semesters[i] = 1
    
    while q:
        c = q.popleft()

        for n in graph[c]:
            indegree[n] -= 1
            
            if indegree[n] == 0:
                q.append(n)
                semesters[n] = semesters[c] + 1
    semesters.remove(0)
    print(' '.join(map(str, semesters)))

topology_sort()