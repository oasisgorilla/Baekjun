import sys
input = sys.stdin.readline

from itertools import combinations

shorts = []

answer = []

for i in range(9):
    shorts.append(int(input().rstrip()))

combis = list(combinations(shorts, 7))

for combi in combis:
    if sum(combi) == 100:
        answer = list(combi)
        break
    else:
        continue

answer.sort()

for num in answer:
    print(num)