import sys

n = int(sys.stdin.readline())

dp = [[0 for _ in range(10)] for _ in range(101)] # 자리수 100개, 앞에 오는 수에 따른 경우의 수

for i in range(1, 10): # dp[1][i] 초기화
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0: # 맨 앞에 오는 수가 0인 경우는 0, 그 이후부터 1이 오는 경우 1개만 셈(x01)
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8] # 9로 시작하는 경우는 8로 끝나는 경우에서만 가능
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] # 이전 자리수에서 위, 아래 숫자로 끝나는 수의 경우 합

print(f"{sum(dp[n]) % 1000000000}")