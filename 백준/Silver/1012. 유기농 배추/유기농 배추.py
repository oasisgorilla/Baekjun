import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, baechu):
    global ans
    q = deque([])
    q.append((x, y))
    baechu[y][x] = -1 # 방문처리
    ans += 1 # 배추 무더기 + 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and baechu[ny][nx] == 1:
                q.append((nx, ny))
                baechu[ny][nx] = -1 # 방문처리
    
    return -1


t = int(input().rstrip()) # 테스트케이스의 수

for _ in range(t): # 테스트 케이스만큼 반복
    m, n, k = map(int, input().split()) # m : 가로, n : 세로, k : 배추 위치

    baechu = [[0 for _ in range(m)] for _ in range(n)] # 배추밭 1 : 배추, 0 : 빈공간, -1 : 방문처리

    ans = 0 # 배추 무더기의 수

    for i in range(k): # 배추의 갯수만큼 배추 배치
        x, y = map(int, input().split())
        baechu[y][x] += 1

    for i in range(n):
        for j in range(m):
            if baechu[i][j] == 1: # 방문하지 않은 배추 무더기만 검사
                # print(f"{j}, {i} 확인")
                bfs(j, i, baechu) # 배열에 맞춰서 전달
            else:
                continue

    print(ans)