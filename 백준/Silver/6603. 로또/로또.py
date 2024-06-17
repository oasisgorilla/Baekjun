import sys
import itertools

input = sys.stdin.readline

test = True

while test:
    inArr = list(map(int, input().split()))
    sLen = inArr[0]
    s = list(inArr[1:])

    if sLen == 0:
        test = False
        break
    for res in itertools.combinations(s, 6):
        print(*res)
    print()