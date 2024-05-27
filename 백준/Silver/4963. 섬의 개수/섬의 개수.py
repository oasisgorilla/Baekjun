import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    dx = [1, 1, 0, -1, -1, -1, 0, 1] # 1, 0 부터 시작해서 시계방향으로 탐색
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    while queue:
        cur = queue.popleft() # 큐에서 탐색할 좌표를 꺼냄
        a = cur[0]
        b = cur[1]
        for i in range(8): # (dx, dy) 쌍의 갯수 8개
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < w and 0 <= ny < h and mapArr[ny][nx] == 1:
                mapArr[ny][nx] = -1 # 인접한 섬의 땅은 방문처리
                queue.append([nx, ny])
                # print(queue)


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    count = 0

    mapArr = []
    for i in range(h):
        mapArr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if mapArr[i][j] == 1:
                bfs(j, i) # bfs로 섬을 방문처리 해준다.
                count += 1

    print(count)