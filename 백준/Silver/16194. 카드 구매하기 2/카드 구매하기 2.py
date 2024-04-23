import sys

n = int(sys.stdin.readline())

dp = [0] + [10000] * (n)
card = [0]

card.extend(map(int, sys.stdin.readline().split()))


for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + card[j])


print(dp[n])
