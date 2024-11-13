import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [x for x in range(n)] # 처음에는 자기 자신을 부모로 설정

def find(x): # x가 속한 집합의 대표 원소를 찾는 함수
    while x != parent[x]: # 초기화된 상태가 아니라면 x의 부모를 따라가며 루트를 찾음
        x = parent[x]
    return x

def union(x, y): # x와 y가 속한 집합을 합치는 함수
    parent_x = find(x)
    parent_y = find(y)
    if parent_x < parent_y: # 대표원소가 더 작은 집합이 부모가 됨
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y

result = 0 # 사이클이 발생한 간선의 번호를 담는 변수

for i in range(1, m+1):
    x, y = map(int, input().split())
    if find(x) == find(y): # x와 y가 같은 집합에 속해있다면 사이클이 발생한 것
        result = i
        break
    union(x, y)

print(result)