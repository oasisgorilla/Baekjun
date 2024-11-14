import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

bfs_answer = []
dfs_answer = []

bfs_visited = [False for _ in range(n + 1)]
dfs_visited = [False for _ in range(n + 1)]

def bfs(start):
    q = deque([start])
    bfs_visited[start] = True
    bfs_answer.append(str(start)) # 노드 탐색 기록

    while q:
        c = q.popleft()
        for n in graph[c]:
            if not bfs_visited[n]:
                q.append(n)
                bfs_visited[n] = True
                bfs_answer.append(str(n))

def dfs(start):
    dfs_answer.append(str(start))
    dfs_visited[start] = True
    
    for n in graph[start]:
        if not dfs_visited[n]:
            dfs(n)

dfs(v)
bfs(v)


print(" ".join(dfs_answer))
print(" ".join(bfs_answer))
