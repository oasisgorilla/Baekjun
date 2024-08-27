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