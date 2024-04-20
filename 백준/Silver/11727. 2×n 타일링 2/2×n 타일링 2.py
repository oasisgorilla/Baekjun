import sys

N = int(sys.stdin.readline())

dp = [0] * 1001 # 경우의 수가 담길 테이블
dp[1] = 1
dp[2] = 3
bricks = [2, 1, 2] # 1 x 2, 2 x 1, 2 x 2 타일별 윗변의 길이

"""
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
"""

for i in range(3, 1001):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

print(f"{dp[N] % 10007}")