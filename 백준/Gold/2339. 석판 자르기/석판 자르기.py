import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = [list(map(int, input().split())) for _ in range(N)]

def solution(board, x0, y0, x1, y1, slice):
    impurities = 0
    jewelry = 0

    # 불순물과 보석 개수를 세는 반복문
    for i in range(x0, x1):
        for j in range(y0, y1):
            if board[i][j] == 1:
                impurities += 1
            elif board[i][j] == 2:
                jewelry += 1
    
    # 보석 하나, 불순물 0이면 경우의 수 1
    if impurities == 0 and jewelry == 1:
        return 1
    
    # 보석 없거나 보석 두 개 이상, 불순물 없으면 경우의 수 0(석판 하나당 보석 하나는 무조건 있어야 함)
    elif jewelry == 0 or (jewelry >= 2 and impurities == 0):
        return 0
    
    ans = 0
    # 불순물 있는 위치에서 자르기
    for i in range(x0, x1):
        for j in range(y0, y1):
            if board[i][j] == 1:
                if slice: # 이전에 세로로 잘랐을 경우
                    if i != x0 and i != x1 - 1:
                        check = True
                        for k in range(y0, y1):
                            if board[i][k] == 2:
                                check = False
                                break
                        if check:
                            ans += solution(board, x0, y0, i, y1, False) * solution(board, i + 1, y0, x1, y1, False)
                else: # 이전에 가로로 자른 경우
                    if j != y0 and j != y1 - 1:
                        check = True
                        for k in range(x0, x1):
                            if board[k][j] == 2:
                                check = False
                                break
                        if check:
                            ans += solution(board, x0, y0, x1, j, True) * solution(board, x0, j + 1, x1, y1, True)
    return ans
        

impurities = sum(row.count(1) for row in board)
jewelry = sum(row.count(2) for row in board)

if impurities == 0 and jewelry == 1:
    print(1)
else:
    resultA = solution(board, 0, 0, N, N, False)
    resultB = solution(board, 0, 0, N, N, True)

    if resultA + resultB == 0:
        print(-1)
    else:
        print(resultA + resultB)