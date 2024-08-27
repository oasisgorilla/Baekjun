"""1트 계수정렬 실패(음수값 고려 안함)"""
# import sys

# input = sys.stdin.readline

# N = int(input().rstrip())

# nums = [False] * 1000001

# for _ in range(N):
#     nums[int(input().rstrip())] = True

# for i in range(1, 1000001):
#     if nums[i] == True:
#         print(i)

"""음수값 고려한 계수정렬(46744kb, 1192mb)"""
import sys

input = sys.stdin.readline

N = int(input().rstrip())

nums = [False] * 2000001

for _ in range(N):
    num = int(input().rstrip())
    nums[num + 1000000] = True

for i in range(2000001):
    if nums[i] == True:
        print(i - 1000000)

"""sort사용한 코드(76972kb, 1384mb)"""
# import sys

# input = sys.stdin.readline

# N = int(input().rstrip())

# nums = []

# for _ in range(N):
#     nums.append(int(input().rstrip()))

# nums.sort()

# for i in range(N):
#     print(nums[i])

