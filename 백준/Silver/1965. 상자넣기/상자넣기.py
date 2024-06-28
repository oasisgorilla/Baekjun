import sys

input = sys.stdin.readline

n = int(input().rstrip())

boxArr = list(map(int, input().split()))

dp = [1] * n

dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if boxArr[j] < boxArr[i]: # 지금 보는 i 상자와 j번째 상자와 비교
            dp[i] = max(dp[i], dp[j] + 1) # i 가 더 크면 넣을 수 있다.
        

# print(dp)
print(max(dp))
