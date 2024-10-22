"""2트(dfs)"""

import sys
input = sys.stdin.readline

M, N, K = map(int, input().rstrip().split()) # y, x, 직사각형 개수

square = []
paper = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
                paper[i][j] = 1

visited = [[False for _ in range(N)] for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    stack = [(x, y)]
    visited[y][x] = True

    size = 1

    while stack:
        cx, cy = stack.pop()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and paper[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((nx, ny))
                size += 1

    return size
               
areas = []

for i in range(M):
     for j in range(N):
          if paper[i][j] == 0 and not visited[i][j]:
               area = dfs(j, i)
               areas.append(area)

areas.sort()
print(len(areas))
print(" ".join(map(str, areas)))