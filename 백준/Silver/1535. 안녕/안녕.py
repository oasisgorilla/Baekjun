import sys
input = sys.stdin.readline

N = int(input().strip())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0] * 101 # 체력이 i일 때 얻을 수 있는 최대 기쁨

for i in range(N):
    for j in range(99, L[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(max(dp))
        