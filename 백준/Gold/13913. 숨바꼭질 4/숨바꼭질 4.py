"""복습"""
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

# visited = [False] * 100001 # 방문체크 불필요
dist = [0] * 100001 # 거리 저장
move = [0] * 100001 # 이전 노드 저장

def bfs(x):
    q = deque([x])
    # visited[x] = True

    while q:
        c = q.popleft()
        if c == K:
            print(dist[c])
            path(c)
            return

        for i in (c + 1, c - 1, 2 * c):
            if 0 <= i <= 100000 and dist[i] == 0: # 범위 내에 있으며, 방문한 적 없는 노드
                q.append(i)
                dist[i] = dist[c] + 1
                move[i] = c

def path(x):
    temp = x
    arr = [] # 경로를 담을 arr

    for _ in range(dist[x] + 1): # x까지 이동한 거리 1초마다 경로 출력
        arr.append(temp)
        temp = move[temp] # 이전 경로를 담는다.
    print(' '.join(map(str, arr[::-1])))

bfs(N)