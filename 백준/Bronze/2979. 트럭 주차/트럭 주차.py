import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

real_time = [0 for _ in range(101)]

for _ in range(3):
    at, lt = map(int, input().split()) # at : 도착시간, lt : 떠난시간
    
    for i in range(at, lt):
        real_time[i] += 1

answer = 0

for tick in real_time:
    if tick == 3:
        answer += C * 3
    elif tick == 2:
        answer += B * 2
    elif tick == 1:
        answer += A
    else:
        continue

print(answer)