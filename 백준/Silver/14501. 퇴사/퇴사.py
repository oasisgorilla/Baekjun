import sys

n = int(sys.stdin.readline())

workTable = [] # 상담 일정표

for i in range(n):
    workTable.append(list(map(int, sys.stdin.readline().split())))

# workTable[i][0] = t, workTable[i][1] = p

dp = [0 for _ in range(n + 1)]

for i in range(n): # i날에 상담을 했을 때
    for j in range(i + workTable[i][0], n + 1): # i날에 일을 했다면 i + workTable[i][0] 날이 된다.
        if dp[j] < dp[i] + workTable[i][1]: # i + workTable[i][0] 날에서, 이전 i에서 계산했던 봉급과 현재 i에서 계산한 봉급을 비교하여 max를 넣는다.
            dp[j] = dp[i] + workTable[i][1]
            # print(f"i = {i}, {dp}")

print(dp[-1])