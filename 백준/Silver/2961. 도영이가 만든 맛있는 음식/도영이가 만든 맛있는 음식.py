import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input().rstrip())

ingredients = []

for _ in range(N):
    ingredients.append(tuple(map(int, input().rstrip().split()))) # 신만, 쓴맛

diff = int(1e9)

for i in range(1, N + 1):
    for comb in combinations(ingredients, i):
        sour = 1
        bitter = 0
        for s, b in comb:
            sour *= s
            bitter += b
        diff = min(diff, abs(sour - bitter))

print(diff)