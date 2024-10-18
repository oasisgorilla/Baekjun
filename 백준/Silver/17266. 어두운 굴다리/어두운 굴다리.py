"""4트"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
x = list(map(int, input().rstrip().split()))

length = 0

if M == 1: # 가로등이 한 개인 경우
    length = max(x[0], N - x[0]) # 시작점-가로등, 가로등-끝점 중 긴 길이

else:
    for i in range(M): # 가로등 수만큼 반복
        if i == 0: # 맨 처음 가로등
            temp = x[i]

        elif i == M - 1: # 맨 마지막 가로등
            temp = N - x[i]

        else:
            distance = x[i] - x[i - 1]

            if distance % 2 == 0:
                temp = distance // 2
            
            else:
                temp = distance // 2 + 1

        length = max(temp, length)

print(length)
