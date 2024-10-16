import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split()) # 식탁의 길이, 거리

burger = input().rstrip()

visit = [False for _ in range(N)]

count = 0

for i in range(N):
    if burger[i] == 'P':
        for j in range(2*K + 1): # 왼쪽 먼 곳부터 확인
            if i - K + j >= 0 and i - K + j < N and burger[i - K + j] == 'H' and visit[i - K + j] == False: # 범위 안에 있으면서, 햄버거면서, 먹지 않았던 버거
                visit[i - K + j] = True
                count += 1
                # print(f"i = {i}, count = {count}")
                break
            else:
                continue

print(count)