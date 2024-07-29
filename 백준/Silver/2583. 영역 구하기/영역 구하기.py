import sys

from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split()) # m : 세로, n : 가로, k : 직사각형 개수

visited = [[0 for _ in range(n)] for _ in range(m)] # 0 : 미방문, 1 <= : 방문

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) # 1 : 좌하, 2 : 우상
    
    """
    아래 for 문에서 처음에 범위를 y2, y1로 설정해줘서 오류가 났었음.
    for문으로 직사각형을 그리면 무조건 위에서 아래로 내려가게 그려질거라는 나의 착각
    위로 그려질 수도 있다. 무조건 작은값이 시작이고, 큰 값이 끝이다.
    """
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] += 1 # 직사각형이 그려진 곳은 방문처리


def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    area = 1 # 면적

    while queue:
        cy, cx = queue.popleft()
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < m) and (0 <= nx < n) and visited[ny][nx] == 0: # 범위 안에 있으면서, 미방문일 경우
                visited[ny][nx] = 1
                queue.append((ny, nx))
                area += 1
    return area

results = [] # 빈공간의 넓이를 담을 배열

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] += 1
            results.append(bfs(i, j))

print(len(results))
print(*sorted(results))


