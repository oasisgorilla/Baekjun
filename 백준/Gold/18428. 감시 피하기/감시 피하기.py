import sys
import copy
from itertools import combinations
input = sys.stdin.readline

N = int(input().rstrip())

corridor = []

for _ in range(N):
    corridor.append(list(map(str, input().split())))

def check_path(corridor): # T의 시야에 S가 들어오는지 확인하는 함수
    for i in range(N):
        for j in range(N):
            if corridor[i][j] == 'T':
                # T의 시야 확인
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nx, ny = i, j
                    while 0 <= nx < N and 0 <= ny < N:
                        if corridor[nx][ny] == 'O':
                            break
                        if corridor[nx][ny] == 'S':
                            return False
                        nx += dx
                        ny += dy
    return True

field = [(i, j) for i in range(N) for j in range(N) if corridor[i][j] == 'X'] # O를 놓을 공간 리스트 생성

answer = False

for comb in combinations(field, 3):
    temp = copy.deepcopy(corridor)
    for x, y in comb:
        temp[x][y] = 'O'
    
    if check_path(temp):
        print("YES")
        break
else:
    print("NO")