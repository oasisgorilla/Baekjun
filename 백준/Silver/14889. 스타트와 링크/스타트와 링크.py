import sys
from itertools import combinations
n = int(sys.stdin.readline())

stat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 조합에 따른 능력치 input
"""
대각선 대칭인 두 수의 합을 골라야 한다
0 0 1 2
0 0 0 0
1 0 0 0
2 0 0 0
위 배열의 두 개의 1은 우하향 대각선 대칭이다.
두 개의 2도 대각선 대칭이다.
팀 숫자만큼 대각선 대칭의 합을 구해야 하는데,
이때 더하는 값들이 위에처럼 같은 줄, 칸에 있으면 안된다.
0 2 0 0
2 0 0 0
0 0 0 1
0 0 1 0
이런 식으로 같은 줄, 칸에 있지 않은 조합을 찾아야 서로 다른 팀이다.

여기서는 sum_stat으로 우하향하는 대각선을 따라 십자가 모양으로 더한 값들의 배열을 만들어준다.
전체 팀 스텟의 합 // 2 를 하여 이상적인 팀스텟을 만들고, 각 십자가 모양은 1번과 나머지, 2번과 나머지...
팀 스텟의 합이 된다.

이 합들을 뽑아서 비교해주는 것이 곧 각 팀원을 뽑아서 비교하는 것과 같다.
"""
sum_stat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))] # 모든 사람의 능력치 조합 - 
# print(sum_stat)
allstat = sum(sum_stat) // 2 # 전체 원소를 더하는 것은 스타트팀, 링크팀 모두의 능력치 합이다.
result = float('inf')
for i in combinations(sum_stat, n // 2): # 대각선 합에서 한 팀의 인원수만큼 
    result = min(result, abs(allstat - sum(i))) # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start 팀 - link 팀

print(result)