import sys

input = sys.stdin.readline

n = int(input().rstrip()) # 1 <= n <= 5000000

wordArr = str(input().rstrip())

num = 0

result = 0

is_num = False

for i in range(n):
    if wordArr[i].isdigit():
        num = num * 10 + int(wordArr[i])
        is_num = True
    else:
        result += num
        num = 0
        is_num = False

if is_num:
    result += num

print(result)