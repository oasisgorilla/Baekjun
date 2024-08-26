import sys
input = sys.stdin.readline

N = int(input().rstrip())

count = [0] * 10001 # 1부터 10000까지 수의 빈도를 저장

for i in range(N):
    num = int(input().rstrip())
    count[num] += 1

for i in range(1, 10001):
    if count[i] > 0:
        for j in range(count[i]):
            print(i)
