import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())

charArr = list(map(str, sys.stdin.readline().split()))

charArr.sort()

resArr = list(combinations(charArr, l)) # charArr에서 l만큼 뽑아야 함


for i in range(len(resArr)):
    zaumCnt = 0
    moumCnt = 0
    # i번째 리스트가 1개 이상의 모음과 2개 이상의 자음을 포함하는지 판별
    for j in resArr[i]:
        if j in 'aeiou':
            moumCnt += 1
        else:
            zaumCnt += 1
    
    if moumCnt >= 1 and zaumCnt >= 2:
        print(''.join(resArr[i]))