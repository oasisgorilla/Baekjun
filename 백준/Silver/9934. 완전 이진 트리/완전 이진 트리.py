import sys
input = sys.stdin.readline

def tree(arr, depth, result):
    if not arr:
        return
    mid = len(arr) // 2 # 루트 노드 찾기
    result[depth].append(arr[mid])
    # 양쪽 자식 노드 탐색
    tree(arr[:mid], depth + 1, result)
    tree(arr[mid + 1:], depth + 1, result)


K = int(input().strip()) # 트리 레벨
visited = list(map(int, input().split()))

result = [[] for _ in range(K)]
tree(visited, 0, result)

for i in result:
    print(' '.join(map(str, i)))