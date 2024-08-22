import sys
input = sys.stdin.readline

N = int(input().rstrip())

room = [input().rstrip() for _ in range(N)]

horiz = 0
verti = 0

# 가로 방향 탐색
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                horiz += 1
            cnt = 0
    if cnt >= 2:
        horiz += 1

# 세로 방향 탐색
for j in range(N):
    cnt = 0
    for i in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                verti += 1
            cnt = 0
    if cnt >= 2:
        verti += 1

print(f"{horiz} {verti}")
