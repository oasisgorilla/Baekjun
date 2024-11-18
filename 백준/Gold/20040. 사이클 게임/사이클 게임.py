import sys
input = sys.stdin.readline

def find_parents(x):
    while parents[x] != x:
        x = parents[x]
    return x

def union(x, y): # x와 y가 속한 집합을 합친다.
    x_parents = find_parents(x)
    y_parents = find_parents(y)

    if x_parents < y_parents:
        parents[y_parents] = x_parents
    else:
        parents[x_parents] = y_parents

n, m = map(int, input().split()) # 점의 개수, 차례 수

parents = [i for i in range(n)] # 처음에는 자기 자신을 부모로 설정
answer = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())

    if find_parents(a) == find_parents(b):
        answer = i
        break
    else:
        union(a, b)

print(answer)