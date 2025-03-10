import sys
input = sys.stdin.readline

INF = float('inf')

N = int(input().strip())
blocks = input().strip()

dp = [INF] * N
dp[0] = 0

for i in range(N):
    if dp[i] == INF: # 순서 안 맞는 경우 건너 뜀
        continue

    current = blocks[i]
    next_block_must_be = 'O'
    if current == 'O':
        next_block_must_be = 'J'
    elif current == 'J':
        next_block_must_be = 'B'
    
    for j in range(i + 1, N):
        if blocks[j] == next_block_must_be:
            cost = (j - i) ** 2
            dp[j] = min(dp[j], dp[i] + cost)

# print(dp)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])