import sys

input = sys.stdin.readline
n = int(input().rstrip())
sam = []
dp_sam = []
for i in range(n):
    sam.append(list(map(int, input().split())))
    dp_sam.append([0 for _ in range(len(sam[i]))]) # 삼각형 dp테이블

dp_sam[0][0] = sam[0][0] # 첫번째 인자 채워주기

for i in range(1, n):
    for j in range(len(sam[i])):
        if j == 0: # 현재 층 첫번째라 왼쪽 위가 없는 경우
            dp_sam[i][j] = max(dp_sam[i][j], sam[i][j] + dp_sam[i - 1][j])
        elif j == len(sam[i]) - 1: # 현재 층 마지막이라 오른쪽 위가 없는 경우
            dp_sam[i][j] = max(dp_sam[i][j], sam[i][j] + dp_sam[i - 1][j - 1])
        else: # 오른쪽, 왼쪽 위가 모두 있는 경우
            dp_sam[i][j] = max(dp_sam[i][j], sam[i][j] + dp_sam[i - 1][j], sam[i][j] + dp_sam[i - 1][j - 1])

print(max(dp_sam[-1]))