# import sys

# from itertools import permutations

# import copy

# n = int(sys.stdin.readline())

# myArr = list(map(int, sys.stdin.readline().split()))

# sortedArr =  copy.deepcopy(myArr) # 첫번째 순열

# sortedArr.sort()

# allArr = list(permutations(sortedArr, n)) # 받은 순열의 원소들로 가능한 모든 조합(사전순 정렬됨)리스트

# resArr = [] # allArr 안에 튜플로 되어 있는 원소들을 list로 바꿔 저장

# for item in allArr:
#     resArr.append(list(item))


# for i in range(len(resArr)):
#     if myArr == resArr[-1]:
#         print(-1)
#     elif myArr == resArr[i]:
#         print(resArr[i + 1])

"""2트"""
import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

find = False # 순열을 찾았는지 여부

for i in range(n - 1, 0, -1): # 맨 뒤부터 시작하면 원소가 증가하다 감소한다.(감소하기만 하면 첫번째, 증가하기만하면 마지막 순열)
    if arr[i - 1] < arr[i]: # 다음에 볼 원소가 현재 보고 있는 원소보다 작을 때(증가하다 감소하는 포인트 i)
        for j in range(n - 1, 0, -1): # i - 1 인덱스보다 큰 원소들 중 가장 작은 원소를 찾기 위해 다시 맨 끝에서 출발
            if arr[i - 1] < arr[j]: # i번째 원소보다 큰 값 중 가장 오른쪽에 있는 값을 찾음
                arr[i - 1], arr[j] = arr[j], arr[i - 1] # 해당 값과 i - 1 원소를 바꿔줌

                arr = arr[:i] + sorted(arr[i:]) # i원소부터 맨 뒤까지 원소를 오름차순으로 바꿔준다.
                for i in arr: # 출력
                    print(i, end=' ')
                exit()
                

print(-1) # for문을 끝까지 돌았으면 - 1이 나오게 한다. 만약 for문에서 끝나는 점을 0이 아니라 -1로 해버리면 54321 케이스에서 i = 5가 되고 sorted(arr[i:])에서 12345가 되어 버린다.
