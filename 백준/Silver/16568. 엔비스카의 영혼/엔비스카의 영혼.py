"""2트"""
import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

dp = [int(1e9) for _ in range(N + 1)]

dp[N] = 0 # 줄의 마지막 위치에서 시작(0초 소요)

for i in range(N, -1, -1):
    if i - 1 >= 0:
        dp[i - 1] = min(dp[i - 1], dp[i] + 1) # 1초 기다리기
    if i - a - 1>= 0:
        dp[i - a - 1] = min(dp[i - a - 1], dp[i] + 1) # a명 앞으로 새치기
    if i - b - 1>= 0:
        dp[i - b - 1] = min(dp[i - b - 1], dp[i] + 1) # b명 앞으로 새치기

# print(dp)
print(dp[0])