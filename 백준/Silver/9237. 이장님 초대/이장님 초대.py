"""1트 실패"""
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())

# sapling = list(map(int, input().split()))

# sapling.sort(reverse=True)

# answer = 0

# for i in range(N, 0, -1):
#     answer += -(min(0, i - sapling[i - 1])) 

# print(f"{answer + N - 1}")

"""2트(그리디, 42036kb, 88ms)"""
import sys

input = sys.stdin.readline

N = int(input().rstrip())

trees = list(map(int, input().split()))

trees.sort(reverse=True)

answer = 0

for i in range(N):
    answer = max(answer, trees[i] + i) # 나무 자라는데 필요한 일 수 + 나무 심느라 지난 일 수

print(f"{answer + 2}") # 심는날 + 다 자란 다음날 = 2일
