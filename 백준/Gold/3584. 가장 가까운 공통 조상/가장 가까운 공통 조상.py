import sys
input = sys.stdin.readline

T = int(input().rstrip())

def find_parent(node, parent): # 부모를 찾고자 하는 노드와 parent 배열을 받음
    # 부모노드를 추적하여 루트노드를 찾을 때까지 진행
    path = [] # 현재 노드부터 루트노드까지의 경로 저장
    while node != -1: # -1은 루트노드이다.
        path.append(node)
        node = parent[node] # node = 파라미터로 받은 node의 부모노드
    return path

for _ in range(T):
    N = int(input().rstrip())
    parent = [-1] * (N + 1) # 부모 정보

    for _ in range(N - 1):
        A, B = map(int, input().split())
        parent[B] = A # B의 부모는 A이다.
    
    X, Y = map(int, input().split())

    # X, Y의 조상 경로 찾기
    X_path = find_parent(X, parent)
    Y_path = find_parent(Y, parent)

    for i in range(len(Y_path)):
        if Y_path[i] in X_path: # Y에서 가장 가까운 조상부터 X에 있는지 확인
            print(Y_path[i])
            break
