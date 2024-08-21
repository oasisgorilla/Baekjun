import sys

input = sys.stdin.readline

N = int(input().rstrip())

myArr = []

for _ in range(N):
    myArr.append(int(input().rstrip()))

myArr.sort(reverse=False)

for num in myArr:
    print(num)