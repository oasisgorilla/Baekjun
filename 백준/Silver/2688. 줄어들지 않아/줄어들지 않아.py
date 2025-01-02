import sys
input = sys.stdin.readline

T = int(input().strip())

dp = [[0 for _ in range(11)] for _ in range(65)]

for i in range(1, 11): # 1, 2의 자리 dp테이블 채우기
    dp[0][i] = 1
    dp[1][i] = 11 - i

for i in range(2, 65):
    for j in range(1, 11):
        dp[i][j] = sum(dp[i - 1]) - sum(dp[i - 1][:j])

# print(f"dp = {dp}")
for _ in range(T):
    n = int(input().strip())
    print(sum(dp[n - 1]))