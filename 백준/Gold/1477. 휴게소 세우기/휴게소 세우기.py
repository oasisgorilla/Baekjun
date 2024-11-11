import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())

areas = list(map(int, input().split()))

areas.append(0)
areas.append(L)
areas.sort()

def construct(max_dist):
    count = 0
    for i in range(1, len(areas)):
        dist = areas[i] - areas[i - 1]
        # 중간 휴게소를 추가하여 max_dist 이하로 만들기 위해 필요한 휴게소 수 계산
        count += (dist - 1) // max_dist
    
    return count <= M

left, right = 1, L
answer = 0

while left <= right: 
    mid = (left + right) // 2

    if construct(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)