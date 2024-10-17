import sys

input = sys.stdin.readline

N = int(input().rstrip()) # 도시의 개수

bridge = list(map(int, input().rstrip().split())) # 두 도시를 연결하는 도로의 길이

city = list(map(int, input().rstrip().split())) # 도시별 주유소 가격

min_price = city[0] # 가장 처음 도시의 기름값으로 초기화

answer = 0

for i in range(N - 1): # 다리의 수만큼 이동
    if i == 0: # 첫번째 도시에서는 무조건 첫번째 도로만큼 넣어야 함
        answer += min_price * bridge[i]
    else:
        if city[i] < min_price: # 다음번 도시 기름값이 더 싸면 최소 기름값 갱신
            min_price = city[i]
            answer += min_price * bridge[i]
        else:
            answer += min_price * bridge[i]

print(answer)