import sys

n = int(sys.stdin.readline()) # 갖고자 하는 카드

cardPrice = [0]


cardPrice.extend(map(int, sys.stdin.readline().split()))


# print(cardPrice)

dpTable = [0] * (n + 1)

for i in range(1, n + 1): # dpTable 커서
    for j in range(1, i + 1): # 현재 채우고 있는 dpTable커서 까지의 j
        # 카드 i 개를 사는 최대 가격은 P_j 카드팩을 사는 경우와 j - i 최대가격 + P_i 카드팩 가격이다.
        dpTable[i] = max(dpTable[i], dpTable[i - j] + cardPrice[j])

print(dpTable[n])