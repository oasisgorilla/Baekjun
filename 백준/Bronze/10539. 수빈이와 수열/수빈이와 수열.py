import sys
input = sys.stdin.readline

N = int(input().rstrip())
num_list = list(map(int, input().split()))

dp = [0] * N
dp[0] = num_list[0]

for i in range(1, N):
    dp[i] = num_list[i] * (i + 1) - sum(dp[:i])

print(*dp)