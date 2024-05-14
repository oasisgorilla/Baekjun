import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())

charArr = list(map(str, sys.stdin.readline().split()))

charArr.sort() # 받은 문자열을 알파벳 오름차순으로 정렬

resArr = list(combinations(charArr, l)) # charArr에서 l만큼 뽑아서 조합 만들기


for i in range(len(resArr)):
    zaumCnt = 0
    moumCnt = 0
    # i번째 리스트가 1개 이상의 모음과 2개 이상의 자음을 포함하는지 판별
    for j in resArr[i]:
        if j in 'aeiou': # 모음 string 안에 reaArr[i] 암호조합 글자가 있는지 확인
            moumCnt += 1 # 있으면, 모음 개수 증가
        else:
            zaumCnt += 1 # 없으면 해당 암호조합의 글자는 모음이 아닐 것이므로, 자음 개수 증가
    
    if moumCnt >= 1 and zaumCnt >= 2: # 모음 1개, 자음 2개 이상이면 해당 암호 조합 출력
        print(''.join(resArr[i]))