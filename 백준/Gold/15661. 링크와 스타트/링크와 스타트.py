import sys

from itertools import combinations

n = int(sys.stdin.readline())

m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

scoreArr = [sum(i) + sum(j) for i, j in zip(m, zip(*m))]

allScore = sum(scoreArr)

minResult = float('inf') # 최솟값

##################################
# scoreArr에서 두 개의 조합으로 나누어서 각 조합의 차이를 출력하는 코드
lenScoreArr = len(scoreArr)

for i in range(1, n//2 + 1):  # i는 1부터 n//2까지 (팀 간 최소 1명 이상 포함)
    for comb1 in combinations(range(n), i):  # index를 사용하여 조합 생성
        team1 = list(comb1)
        team2 = [x for x in range(n) if x not in team1]
        
        sum1 = sum(scoreArr[j] for j in team1)
        sum2 = sum(scoreArr[j] for j in team2)
        
        diff = abs(sum1 - sum2) // 2
        minResult = min(minResult, diff)

print(minResult)