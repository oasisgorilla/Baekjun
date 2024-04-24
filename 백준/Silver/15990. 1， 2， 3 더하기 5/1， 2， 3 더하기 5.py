import sys

t = int(sys.stdin.readline()) # 테스트 케이스 개수

dp = [[0, 0, 0] for _ in range(100001)]  # 2차원 배열 dp 정의

# ~ +1, ~ +2, ~ +3으로 끝나는 경우의 수
dp[1] = [1, 0, 0] # 1은 2나 3으로 끝날 수 없다.
dp[2] = [0, 1, 0] # 1+1 은 연속된 두 수이기 때문에 불가능
dp[3] = [1, 1, 1]

for i in range(4, len(dp)): # 1, 2, 3을 미리 채워놔서 4부터 시작
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009 # (i - 1) + 1  조합 수, ~ + 1 = 3 의 경우는 제외(~ + 1 + 1 이면 1이 연속된 두 수가 된다.)
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009 # (i - 2) + 2 조합 수에서 ~ + 2 인 경우 제외
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009 # (i - 3) + 3 조합 수에서 ~ + 3 인 경우 제외

for i in range(t):
    n = int(sys.stdin.readline())
    print(f"{(dp[n][0]+dp[n][1]+dp[n][2]) % 1000000009}")