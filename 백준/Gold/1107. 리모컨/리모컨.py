import sys

n = int(sys.stdin.readline()) # 가고자 하는 채널

m = int(sys.stdin.readline()) # 고장난 버튼의 개수

arr = list(map(int, sys.stdin.readline().split()))

min_click = abs(n - 100) # 최소 버튼 클릭 초기화

# 주어진 n값이 500000(최대 input)이고, 남은 버튼이 6인 경우, 666666에서 내려와야 함,
# 이때 최악의 경우는 9만 남아서 999999에서 내려와야 하는 경우이므로, range는 0 ~ 999999이다. 
for channel in range(1000000):
    for digit in str(channel):
        if int(digit) in arr:
            break
    else:
        min_click = min(min_click, len(str(channel)) + abs(n - channel))

print(min_click)