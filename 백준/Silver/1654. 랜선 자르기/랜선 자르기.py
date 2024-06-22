import sys

input = sys.stdin.readline

k, n = map(int, input().split()) # 항상 k <= n

lanLen = [int(input().rstrip()) for _ in range(k)]

left, right = 1, max(lanLen)

def total(div):
    res = 0
    for i in lanLen:
        res += i // div # 케이블 각각의 길이를 div로 나눈 후 모두 더함
    
    return res

while left <= right:
    mid = (left + right) // 2 # 랜선 길이

    totalLan = total(mid) # 랜선 갯수

    if totalLan >= n: # 랜선 길이에 따른 랜선 갯수로 이분탐색
        left = mid + 1
    else:
        right = mid - 1

print(right)
