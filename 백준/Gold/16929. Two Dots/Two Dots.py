import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

gamePan = []
idx = 2
for i in range(n):
    gamePan.append(list(input().rstrip()))
    idx += m
# print(gamePan)
visited = [[0] * m for _ in range(n)]

def dfs(y, x, from_y, from_x, color):
    if visited[y][x]:
        return True
    
    visited[y][x] = True
    
    dx = [1, 0, -1, 0] # 오른쪽, 아래, 왼쪽, 위
    dy = [0, 1, 0, -1]
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < m and gamePan[ny][nx] == color:
            if not visited[ny][nx]:
                if dfs(ny, nx, y, x, color):
                    return True
            elif ny != from_y or nx != from_x:
                return True
    
    return False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, -1, -1, gamePan[i][j]):
                print("Yes")
                sys.exit()

print("No")