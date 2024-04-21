import sys

N = int(sys.stdin.readline())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 1]

print(f"{dp[N] % 10007}")