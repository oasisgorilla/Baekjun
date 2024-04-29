import sys

n = int(sys.stdin.readline())

# 색상 받기

color = [[0, 0, 0]] # 0 : r, 1 : g, 2 : b

for i in range(n):
     color.append(list(map(int, sys.stdin.readline().split())))

dp = [[0, 0, 0] for _ in range(1001)]

dp[1] = color[1] #color로 받은 첫번째 집 칠비용

for i in range(2, n + 1): # 2부터 최솟값 조합 저장
     for j in range(3):
          dp[i][j] = min(dp[i - 1][j - 2] + color[i][j], dp[i - 1][j - 1] + color[i][j])

min = 0

if dp[n][0] > dp[n][1]:
     min = dp[n][1]
else:
     min = dp[n][0]

if min > dp[n][2]:
     min = dp[n][2]

print(min)
