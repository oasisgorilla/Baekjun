import sys
input = sys.stdin.readline

N = int(input().strip())

univs = ['']
for _ in range(N):
    univs.append(str(input().strip()))

first = [i for i in range(N + 1)] # 다음 이름의 첫번째
last = [i for i in range(N + 1)] # 지금 이름의 마지막

for _ in range(N - 1):
    a, b = map(int, input().split())

    first[last[a]] = b # 지금 이름 i의 다음 이름 j
    last[a] = last[b] # j를 i에 통합

for i in range(N):
    print(univs[a], end='')
    a = first[a] 