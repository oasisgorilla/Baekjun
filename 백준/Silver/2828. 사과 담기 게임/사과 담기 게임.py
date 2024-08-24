import sys

input = sys.stdin.readline

N, M = map(int, input().split())

J = int(input().rstrip())

apple = []

basket = 1

answer = 0

for _ in range(J):
    apple.append(int(input().rstrip()))

for i in range(len(apple)):
    if basket <= apple[i] <= basket + M - 1:
        continue
    elif basket > apple[i]:
        move = basket - apple[i]
        answer += move
        basket -= move
    elif basket + M - 1 < apple[i]:
        move = apple[i] - (basket + M - 1)
        answer += move
        basket += move

print(answer)
