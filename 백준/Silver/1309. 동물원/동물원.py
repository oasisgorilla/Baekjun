import sys

n = int(sys.stdin.readline())

dp = [[0, 0, 0] for _ in range(n)]

# dp[0] : 양쪽 칸에 사자 없음
# dp[1] : 왼쪽 칸에 사자
# dp[2] : 오른쪽 칸에 사자

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, n): # 2 * 2 칸을 채우는 경우 부터
    for j in range(3):
        if j == 0:
            dp[i][j] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
        elif j == 1:
            dp[i][j] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
        else:
            dp[i][j] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n - 1]) % 9901)