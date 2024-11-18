# from itertools import combinations

"""1트(시간초과)"""
# def solution(n, s):
#     # 합이 s가 되는 자연수 n개로 이루어진 집합
    
#     # 최고의 집합이 존재하지 않는 경우, -1이 담긴 집합 반환
#     if n > s:
#         return [-1]
#     answer = []
#     # 최고의 집합은 모든 원소들의 차이가 가장 적게 나는 집합이다.
#     # 먼저 같은 원소들로 이루어진 경우가 제일 우선이다.
#     if s % n == 0:
#         answer = [s//n for _ in range(n)]
#         return answer
#     # 아닌 경우 그 근사치의 숫자를 갖고 있으면 최고의 집합이다.
#     key = s // n
#     nums = [num for num in range(1, s+1-(n-1))]
#     for comb in combinations(nums, n):
#         if sum(comb) == s:
#             if key in set(comb):
#                 answer = comb
#     # answer = []
#     return answer

"""2트"""
def solution(n, s):
    if n > s:
        return [-1]
    
    base_num = s // n
    
    answer = [base_num for _ in range(n)]
    
    if s % n > 0:
        for i in range(s % n):
            answer[i] += 1
    
    answer.sort() # 정렬
    return answer