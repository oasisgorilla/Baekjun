import sys

n, k = map(int, sys.stdin.readline().split()) # 최종 합 n, 합의 구성원 수 k

dp = [[0] * (k + 1) for i in range(n + 1)] # dp[n][k] 테이블 선언, 초기화
dp[0][0] = 1 # 0을 0으로 만드는 경우 1개

for i in range(n + 1):
    for j in range(1, k + 1): # 0 이외의 다른 수를 0개의 조합으로 만드는 경우는 없다.
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[-1][-1] % 1000000000)