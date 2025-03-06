import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = []
for _ in range(N):
    K.append(int(input().strip()))

left = min(K)
right = sum(K)
answer = right

while left <= right:
    mid = (left + right) // 2
    curr = mid
    count = 1 # 인출 횟수

    for cash in K:
        if curr < cash: # 인출 금액보다 써야될 금액이 큰 경우
            curr = mid # curr 초기화
            count += 1 # 모자라는 금액을 집어넣고 인출
        curr -= cash
    
    if count > M or mid < max(K):
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)