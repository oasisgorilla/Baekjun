import sys
input = sys.stdin.readline

D, K = map(int, input().split())

dp = [0 for _ in range(D + 1)]

for i in range(1, K + 1):
    for j in range(i, K + 1):
        dp[1] = i
        dp[2] = j

        for k in range(3, D + 1):
            dp[k] = dp[k - 1] + dp[k - 2]
        
        if dp[D] == K:
            print(i)
            print(j)
            exit()