import sys

n = int(sys.stdin.readline()) # 가고자 하는 채널

m = int(sys.stdin.readline()) # 고장난 버튼의 개수

arr = list(map(int, sys.stdin.readline().split()))

min_click = abs(n - 100) # 최소 버튼 클릭 초기화

for channel in range(1000001):
    for digit in str(channel):
        if int(digit) in arr:
            break
    else:
        min_click = min(min_click, len(str(channel)) + abs(n - channel))

print(min_click)