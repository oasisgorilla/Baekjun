import sys
input = sys.stdin.readline

w, h = map(int, input().split())
x, y = map(int, input().split())

# 토쟁이가 토스트 가게에 가는 경우의 수 + 토스트가게에서 학교로 가는 경우의 수

dp = [[0 for _ in range(w)] for _ in range(h)]
dp[0][0] = 1

# 집 - 토스트
for i in range(y):
    for j in range(x):
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]

# 토스트 - 학교
for i in range(y - 1, h):
    for j in range(x - 1, w):
        if i > y - 1:
            dp[i][j] += dp[i - 1][j]
        if j > x - 1:
            dp[i][j] += dp[i][j - 1]

print(dp[-1][-1] % 1000007)