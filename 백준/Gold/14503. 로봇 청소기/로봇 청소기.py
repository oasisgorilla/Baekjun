import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

roomArr = [] # 1 : 벽, 0 : 빈 칸

startArr = list(map(int, input().split())) # 시작 좌표, 방향

for _ in range(n):
    roomArr.append(list(map(int, input().split())))

cleanArr = copy.deepcopy(roomArr) # 1 : 청소했거나 벽, 0 : 청소 안함

res = 0 # 청소한 칸, 시작할 때 무조건 한 칸 청소함

I, J = startArr[:2] # 현재 좌표
D = startArr[2] # 현재 방향

# 방향: 북(0), 동(1), 남(2), 서(3)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

operation = True
while operation:
    if cleanArr[I][J] == 0: # 현재 칸이 아직 청소되지 않은 경우
        cleanArr[I][J] = 1 # 현재 칸을 청소한다.
        res += 1 # 청소한 칸 카운트

    found_cleanable = False
    for _ in range(4):
        D = (D + 3) % 4 # 반시계 방향으로 회전
        ni, nj = I + di[D], J + dj[D]
        if cleanArr[ni][nj] == 0 and roomArr[ni][nj] == 0: # 청소하지 않은 칸
            I, J = ni, nj
            found_cleanable = True
            break

    if not found_cleanable:
        # 후진
        ni, nj = I - di[D], J - dj[D]
        if roomArr[ni][nj] == 1: # 벽이면 멈춘다
            operation = False
        else:
            I, J = ni, nj

print(res)
