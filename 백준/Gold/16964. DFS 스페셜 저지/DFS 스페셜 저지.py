"""복습"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

seq = list(map(int, input().split()))

"""
dfs를 돌면서 seq[i]와 순서가 일치하는지 확인한다.
확인해야할 순서를 seq[i]에서 주어진대로 강제해야한다.
부모-자식관계를 알 수 있는 데이터가 필요하다.?
"""
parents = [0] * (N + 1) # 각 노드의 부모를 기록할 배열 

# def find_parents():
#     bfs_visited = [False] * (N + 1)
#     q = deque([seq[0]])
#     bfs_visited[seq[0]] = True

#     while q:
#         c = q.popleft()
#         for n in graph[c]:
#             if not bfs_visited[n]:
#                 q.append(n)
#                 bfs_visited[n] = True
#                 parents[n] = c # n의 부모 c를 기록

def check_dfs_seq():
    # find_parents()
    position = [0] * (N + 1) # 각 노드의 방문 순서
    for i, node in enumerate(seq):
        position[node] = i # 노드 node의 방문 순서 i를 기록

    # 탐색 순서 강제
    for i in range(1, N + 1):
        graph[i].sort(key=lambda x : position[x]) # graph[i]의 이웃노드를 각 노드의 방문순서대로 정렬

    # dfs 탐색
    dfs_visited = [False] * (N + 1)
    stk = [1] # 문제에서 시작 정점을 1로 강제함
    dfs_visited[1] = True
    idx = 0
    while stk:
        c = stk.pop()
        # print(f"c : {c}, seq : {seq[idx]}")
        if c != seq[idx]:
            return 0
        
        for n in reversed(graph[c]):
            if not dfs_visited[n]:
                stk.append(n)
                dfs_visited[n] = True
        idx += 1
    return 1

print(check_dfs_seq())