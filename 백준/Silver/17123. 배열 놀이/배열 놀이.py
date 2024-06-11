import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    #################### 입력 #####################
    n, m = map(int, input().split())  # n X n 배열, m 번의 연산
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(m)]

    # 차분 배열 초기화
    diff = [[0] * (n + 1) for _ in range(n + 1)]

    #################### 연산 #####################
    for r1, c1, r2, c2, v in b:
        diff[r1 - 1][c1 - 1] += v
        if r2 < n:
            diff[r2][c1 - 1] -= v
        if c2 < n:
            diff[r1 - 1][c2] -= v
        if r2 < n and c2 < n:
            diff[r2][c2] += v

    # 차분 배열을 사용하여 원래 배열 업데이트
    for i in range(n):
        for j in range(n):
            if i > 0:
                diff[i][j] += diff[i - 1][j]
            if j > 0:
                diff[i][j] += diff[i][j - 1]
            if i > 0 and j > 0:
                diff[i][j] -= diff[i - 1][j - 1]
            a[i][j] += diff[i][j]

    # 행의 합 배열과 열의 합 배열 만들기
    res1 = [sum(row) for row in a]
    res2 = [sum(a[i][j] for i in range(n)) for j in range(n)]

    #################### 출력 #####################
    print(' '.join(map(str, res1)))
    print(' '.join(map(str, res2)))