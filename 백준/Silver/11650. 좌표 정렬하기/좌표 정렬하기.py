import sys

input = sys.stdin.readline

N = int(input().rstrip())

coordinate = []

for i in range(N):
    coordinate.append(tuple(map(int, input().split())))

coordinate.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*coordinate[i])