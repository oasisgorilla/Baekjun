"""1트(코드 잘못 짬)"""

# import sys
# import heapq

# input = sys.stdin.readline

# N = int(input().rstrip()) # 연산의 개수

# x = [] # 연산 정보

# for _ in range(N):
#     x.append(int(input().rstrip()))

# q = []

# abs_max = (0, 0) # 절대값 크기, 인덱스

# for i in range(N):
#     inst = x[i] # 연산
    
#     if inst == 0:
#         if len(q) == 0: # 배열이 빈 경우
#             print(0)
#         else:
#             print(abs_max[0]) # 최대값 출력
#             del x[abs_max[1]] # 값 삭제

#     elif inst < 0:
#         if inst * -1 > abs_max[0]:
#             abs_max = (inst * -1, i) # 최대값 크기와 인덱스 저장
#     else:
#         if inst > abs_max[0]:
#             abs_max = (inst, i)

"""2트(39824kb, 132ms)"""
import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
heap = []

for _ in range(N):
    x = int(input().rstrip())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap, (abs(x), x))