"""3트"""
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(x, y, z): # start = (x, y, z)
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    q = deque([(x, y, z)])
    visited[z][y][x] = True

    while q:
        cx, cy, cz = q.popleft()

        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            
            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                if building[nz][ny][nx] == 'E':
                    distance[nz][ny][nx] = distance[cz][cy][cx] + 1 # 거리 기록
                    print(f"Escaped in {distance[nz][ny][nx]} minute(s).")
                    return
                elif building[nz][ny][nx] == '.' and not visited[nz][ny][nx]:
                    q.append((nx, ny, nz))
                    visited[nz][ny][nx] = True
                    distance[nz][ny][nx] = distance[cz][cy][cx] + 1
    print("Trapped!")
    return
        

def find_start(building):
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    return k, j, i # 이 부분에서 넘겨줄 때 i, j, k 즉 z, y, x 순으로 넘겨주고 있었음

while True:

    L, R, C = map(int, input().split()) # 층, 행, 열

    if L == 0 and R == 0 and C == 0:
        break

    building = [[[]*C for _ in range(R)] for _ in range(L)]

    distance = [[[0]*C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        building[i] = [list(map(str, input().strip())) for _ in range(R)]
        input() # 줄바꿈 받아주기

    # 시작지점 찾기
    sx, sy, sz = find_start(building)
    # print(sx, sy, sz)

    bfs(sx, sy, sz)