import sys
input = sys.stdin.readline

N, M = map(int, input().split())

sector = []

sector.append([0 for _ in range(M + 1)])

for i in range(1, N + 1):
    sector.append(list(map(int, input().split())))

for i in range(1, N + 1):
    sector[i].insert(0, 0)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + sector[i][j]

# print(dp)

K = int(input().strip())

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)