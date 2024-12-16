import sys
input = sys.stdin.readline

N = int(input().strip())

tetra = [0] * 300001 # 완벽한 사면체의 크기
tri = [0] * 300001 # 사면체의 단면 크기

tetra[1] = 1
tri[1] = 1

for i in range(2, 300001):
    tri[i] = tri[i - 1] + i
    tetra[i] = tetra[i - 1] + tri[i]
    if tetra[i] > N:
        break

max_tetra = i if tetra[i] <= N else i - 1

dp = [int(1e9)] * (N + 1)
dp[0] = 0

for t in range(1, max_tetra + 1):
    for j in range(tetra[t], N + 1):
        dp[j] = min(dp[j], dp[j - tetra[t]] + 1)

print(dp[N])