import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

answer = 0

combis = list(combinations(card_list, 3))

for combi in combis:
    if sum(combi) <= M and sum(combi) > answer:
        answer = sum(combi)
    else:
        continue

print(answer)
                 