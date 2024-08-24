import sys

input = sys.stdin.readline

integer = int(input().rstrip())

intList = []

while integer >= 10:
    intList.append(integer % 10)
    integer = integer // 10

intList.append(integer)
intList.sort(reverse=True)

for i in intList:
    print(i, end='')