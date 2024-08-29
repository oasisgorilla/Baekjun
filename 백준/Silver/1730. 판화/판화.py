import sys

input = sys.stdin.readline

N = int(input().rstrip())
directions = input().rstrip()

# N x N 크기의 격자판 초기화
wood = [['.' for _ in range(N)] for _ in range(N)]

# 시작 위치
x, y = 0, 0

for move in directions:
    if move == 'U' and y > 0:
        if wood[y][x] == '.':
            wood[y][x] = '|'
        elif wood[y][x] == '-':
            wood[y][x] = '+'
        y -= 1
        if wood[y][x] == '.':
            wood[y][x] = '|'
        elif wood[y][x] == '-':
            wood[y][x] = '+'
    
    elif move == 'D' and y < N - 1:
        if wood[y][x] == '.':
            wood[y][x] = '|'
        elif wood[y][x] == '-':
            wood[y][x] = '+'
        y += 1
        if wood[y][x] == '.':
            wood[y][x] = '|'
        elif wood[y][x] == '-':
            wood[y][x] = '+'
    
    elif move == 'L' and x > 0:
        if wood[y][x] == '.':
            wood[y][x] = '-'
        elif wood[y][x] == '|':
            wood[y][x] = '+'
        x -= 1
        if wood[y][x] == '.':
            wood[y][x] = '-'
        elif wood[y][x] == '|':
            wood[y][x] = '+'
    
    elif move == 'R' and x < N - 1:
        if wood[y][x] == '.':
            wood[y][x] = '-'
        elif wood[y][x] == '|':
            wood[y][x] = '+'
        x += 1
        if wood[y][x] == '.':
            wood[y][x] = '-'
        elif wood[y][x] == '|':
            wood[y][x] = '+'

# 결과 출력
for row in wood:
    print(''.join(row))

   