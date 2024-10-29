import sys
input = sys.stdin.readline

N = int(input().rstrip())

kids = []

for _ in range(N):
    kids.append(int(input().rstrip()))

dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if kids[j] < kids[i]:
            dp[i] = max(dp[i], dp[j] + 1)

answer = N - (max(dp) + 1)

print(answer)
