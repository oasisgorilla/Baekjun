import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

land = [list(map(int, input().rstrip().split())) for _ in range(n)]

def bfs(start_x, start_y, land):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y)])
    distance = [[-1] * m for _ in range(n)] # 거리를 나타낸 새로운 지도, 갈 수 없는 곳을 먼저 -1로 초기화

    distance[start_y][start_x] = 0 # 시작지점 초기화

    while q:
        x, y, d= q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                if (nx, ny) not in visited and land[ny][nx] == 1: # 방문하지 않았으면서 지도에서 1인 칸
                    visited.add((nx, ny))
                    distance[ny][nx] = d + 1
                    q.append((nx, ny, d + 1))

    for i in range(n):
        for j in range(m):
            if land[i][j] == 0:
                distance[i][j] = 0

    return distance

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            result = bfs(j, i, land)

            for row in result:
                print(" ".join(map(str, row)))
            break

