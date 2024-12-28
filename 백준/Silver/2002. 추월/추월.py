import sys
input = sys.stdin.readline

N = int(input().strip())

# 출발 순서
start_order = [input().strip() for _ in range(N)]

# 도착 순서
end_order = [input().strip() for _ in range(N)]

# 출발 순서를 기준으로 각 차량의 순서를 기록
start_index = {car: i for i, car in enumerate(start_order)}

overtakes = 0

# 도착 순서를 순회하며 추월 여부를 확인
for i in range(N - 1):
    # 출발 순서에서 나보다 앞에 있는 차들 중 아직 도착하지 않은 차가 있다면 추월 발생
    for j in range(i+1, N):
        if  start_index[end_order[i]] > start_index[end_order[j]]:
            overtakes += 1
            break

print(overtakes)