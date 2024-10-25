"""1트(실패, 테스트 케이스부터 틀림)"""

# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split()) # 집하장의 개수, 경로의 개수

# """
# 다익스트라의 경우 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이다.
# 이 경우 모든 경로표를 출력해야하기 때문에 플로이드 워셜 알고리즘을 사용한다.
# """

# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# # 모든 노드경로 표의 시작 지점 거리를 0으로 초기화
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for _ in range(m):
#     # a : 출발, b : 도착, c : 거리
#     a, b, c = map(int, input().split())
#     if c < graph[a][b]: # 더 짧은 간선만 추가
#         graph[a][b] = c
#         graph[b][a] = c # 양방향 처리

# # 플로이드 워셜 알고리즘
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for k in range(1, n + 1):
#             graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

# # 출력
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if graph[i][j] == INF:
#             print('INFINITY', end=' ')
#         else:
#             print(graph[i][j], end=' ')
# print()  

"""2트"""
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split()) # 집하장의 개수, 경로의 개수

# """
# 다익스트라의 경우 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이다.
# 이 경우 모든 경로표를 출력해야하기 때문에 플로이드 워셜 알고리즘을 사용한다.
# """

# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# first_node = [[0] * (n + 1) for _ in range(n + 1)]

# # 모든 노드경로 표의 시작 지점 거리를 0으로 초기화
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# for _ in range(m):
#     # a : 출발, b : 도착, c : 거리
#     a, b, c = map(int, input().split())
#     if c < graph[a][b]: # 더 짧은 간선만 추가
#         graph[a][b] = c
#         graph[b][a] = c # 양방향 처리
#         first_node[a][b] = b
#         first_node[b][a] = a

# # 플로이드 워셜 알고리즘
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for k in range(1, n + 1):
#             graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k]) # 오류가 나는 부분
#             first_node[j][k] = first_node[j][i]

# # 출력
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print('-', end=' ')
#         else:
#             print(first_node[i][j], end=' ')
#     print()

"""3트"""
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 집하장의 개수, 경로의 개수

"""
다익스트라의 경우 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘이다.
이 경우 모든 경로표를 출력해야하기 때문에 플로이드 워셜 알고리즘을 사용한다.
"""

graph = [[INF] * (n + 1) for _ in range(n + 1)]
first_node = [[0] * (n + 1) for _ in range(n + 1)]

# 모든 노드경로 표의 시작 지점 거리를 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a : 출발, b : 도착, c : 거리
    a, b, c = map(int, input().split())
    if c < graph[a][b]: # 더 짧은 간선만 추가
        graph[a][b] = c
        graph[b][a] = c # 양방향 처리
        first_node[a][b] = b
        first_node[b][a] = a

# 플로이드 워셜 알고리즘
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]
                first_node[j][k] = first_node[j][i]

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print('-', end=' ')
        else:
            print(first_node[i][j], end=' ')
    print()
