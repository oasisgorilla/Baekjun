"""2트"""

import sys

input = sys.stdin.readline

n = int(input().rstrip())
numArr = list(map(int, input().split()))

if n == 1:
    print(numArr[0])
    sys.exit()

# dp[i][0]은 i번째까지 원소를 삭제하지 않은 최대 합
# dp[i][1]은 i번째까지 원소를 하나 삭제한 최대 합
dp = [[0] * 2 for _ in range(n)]

# 초기값 설정
dp[0][0] = numArr[0]
dp[0][1] = float('-inf')

result = numArr[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + numArr[i], numArr[i])
    dp[i][1] = max(dp[i-1][1] + numArr[i], dp[i-1][0])
    result = max(result, dp[i][0], dp[i][1])

print(result)