import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 나무의 수 : n, 집에 가져갈 나무 길이 : m

trees = list(map(int, input().split()))

def cut_the_tree(height): # 절단기 가동!!
    timber = 0 # 잘린 나무토막의 총 합
    for tree in trees:
        if tree >= height:
            timber += tree - height

    return timber

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    totalTimber = cut_the_tree(mid) # 지금 설정한 높이일 때 가져가는 나무

    if totalTimber >= m: # 너무 많이 잘랐을 경우
        start = mid + 1 # 덜 자르고
    elif totalTimber < m: # 너무 덜 자른 경우
        end = mid - 1 # 더 자른다
    
print(end)