import sys
INF = 2147000000 # 무한
n = int(sys.stdin.readline()) # 테스트 케이스의 수
rgb = [[0, 0, 0]] # rgb[1]은 1번 집을 칠하는 색
ans = INF # 정답 초기화

for _ in range(n): # 집 칠하는 비용 입력 받기
    rgb.append(list(map(int, sys.stdin.readline().split())))

for i in range(3): # 각 시행에서 시작하는 색이 i인 조합만 계산하여 최솟값 산출/ 갱신
    dp = [[INF, INF, INF] for _ in range(n + 1)] # i 색에 대한 dp테이블 채우기
    dp[1][i] = rgb[1][i] # 첫번째 집 칠하는 비용 채우기
    for j in range(2, n + 1): # j는 집의 개수
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2]) # 각 색별로 테이블 채우기,
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2]) # 다른 색으로 시작한 조합은 도태된다(inf로 초기화 돼있기 때문)
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j: # i 색과 끝 색이 다른 경우만 체크
            ans = min(ans, dp[-1][j]) # 다른 i에서의 최솟값과 비교
print(ans)