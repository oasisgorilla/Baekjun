import sys

n, m = map(int, sys.stdin.readline().split()) # n = 노드 개수 m = 관계 개수
relation = [[] for _ in range(n)] # 인접리스트 작성
visited = [False] * n # 방문한 노드
arrive = False # 5개 노드 탐색 성공 여부

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

def dfs(start, depth):
    global arrive
    visited[start] = True # 시작노드 방문처리

    if depth == 4: # 이어진 다른 노드를 4번 탐색했을 경우
        arrive = True
        return
    for i in relation[start]:
        if visited[i] == False:
            dfs(i, depth + 1) # 이어진 다른 노드 탐색시 depth 상승
    visited[start] = False # 다른 노드 시작일 때를 위해 미방문처리

for i in range(n):
    dfs(i, 0)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)