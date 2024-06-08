import sys

n = int(sys.stdin.readline().rstrip())
def solution(n):
    profit = []
    dp = [0 for _ in range(n)]
    for i in range(n):
        profit.append(int(sys.stdin.readline().rstrip()))

    dp[0] = profit[0]

    for i in range(1, len(profit)):
        dp[i] = max(profit[i], profit[i] + dp[i - 1])
    
    print(max(dp))
    
    return

while n != 0:
    solution(n)
    n = int(sys.stdin.readline().rstrip())