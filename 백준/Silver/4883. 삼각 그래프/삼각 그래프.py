"""3트"""
import sys
input = sys.stdin.readline

k = 0

while True:
    k += 1
    N = int(input().strip())

    if N == 0:
        break
    
    graph = []

    for _ in range(N):
        graph.append(list(map(int, input().split())))

    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][0] = int(1e9)
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1] + graph[0][2]

    for i in range(1, N):
        dp[i][0] = graph[i][0] + min(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = graph[i][1] + min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0])
        dp[i][2] = graph[i][2] + min(dp[i - 1][1], dp[i - 1][2], dp[i][1])
    
    # print(dp)
    print(f"{k}. {dp[N - 1][1]}")