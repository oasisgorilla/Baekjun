import sys
input = sys.stdin.readline

N = int(input().rstrip())

room = []
for i in range(N):
    room.append(list(map(str, input().rstrip())))

visited_x = [[False for _ in range(N)] for _ in range(N)]
visited_y = [[False for _ in range(N)] for _ in range(N)]

def dfs_x(x, y, cnt, visited_x):
    # print(f"dfs_x, x: {x} y: {y} cnt: {cnt}")
    if visited_x[y][x]:
        return cnt

    cnt += 1
    visited_x[y][x] = True
    if x + 1 < N and room[y][x + 1] != 'X' and not visited_x[y][x + 1]:
        return dfs_x(x + 1, y, cnt, visited_x)
    return cnt

def dfs_y(x, y, cnt, visited_y):
    if visited_y[y][x]:
        return cnt
    
    cnt += 1
    visited_y[y][x] = True
    if y + 1 < N and room[y + 1][x] != 'X' and not visited_y[y + 1][x]:
        return dfs_y(x, y + 1, cnt, visited_y)
    return cnt
    

horiz = 0
verti = 0

for i in range(N):
    for j in range(N):
        if room[i][j] != 'X':
            # print(f"탐색 x: {i}, y: {j}, t/f: {visited_y[i][j]}")
            if dfs_x(j, i, 0, visited_x) >= 2:
                horiz += 1
            if dfs_y(j, i, 0, visited_y) >= 2:
                verti += 1

print(f"{horiz} {verti}")
