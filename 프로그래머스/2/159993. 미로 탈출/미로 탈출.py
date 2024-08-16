from collections import deque

def solution(maps):
    new_maps = []
    n = len(maps)
    m = len(maps[0])



    for i in range(n):
        temp_list = list(maps[i])
        new_maps.append(temp_list)

    def bfs(start, target, n, m):
        visited = [[False for _ in range(m)] for _ in range(n)] # bfs 할 때마다 초기화되도록
        distance = [[0 for _ in range(m)] for _ in range(n)]

        q = deque([start]) # start = (0, 0)
        x, y = start
        visited[x][y] = True

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        while q:
            cx, cy = q.popleft()

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != True:
                    if new_maps[nx][ny] != 'X':
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        distance[nx][ny] = distance[cx][cy] + 1

                        if (nx, ny) == target:
                            return distance[nx][ny]
        return -1 # 에러

    start, lever, finish = None, None, None

    for i in range(n):
        for j in range(m):
            if new_maps[i][j] == 'S':
                start = (i, j)
            elif new_maps[i][j] == 'L':
                lever = (i, j)
            elif new_maps[i][j] == 'E':
                finish = (i, j)

    if not start or not lever or not finish:
        return -1

    start_to_lever = bfs(start, lever, n, m)
    if start_to_lever == -1:
        return -1

    lever_to_finish = bfs(lever, finish, n, m)
    if lever_to_finish == -1:
        return -1

    return start_to_lever + lever_to_finish