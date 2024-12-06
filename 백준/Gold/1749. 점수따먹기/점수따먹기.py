import sys
input = sys.stdin.readline

# 입력 처리
n, m = map(int, input().split())
arr = []
idx = 2
for i in range(n):
    arr.append(list(map(int, input().split())))
    idx += m

# 카데인 알고리즘을 사용한 최대 부분 배열 합 계산
max_sum = float('-inf')

# 모든 가능한 행 범위에 대해 탐색
for row_start in range(n):
    # 열 합을 누적하여 1차원 배열로 변환
    col_sum = [0] * m
    for row_end in range(row_start, n):
        for col in range(m):
            col_sum[col] += arr[row_end][col]
        
        # 1차원 배열에서 최대 부분 합을 찾음
        current_max = float('-inf')
        current_sum = 0
        for value in col_sum:
            current_sum = max(value, current_sum + value)
            current_max = max(current_max, current_sum)
        
        # 최대값 갱신
        max_sum = max(max_sum, current_max)

print(max_sum)