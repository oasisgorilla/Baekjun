"""2트"""
import sys
from collections import deque
input = sys.stdin.readline

g, S = map(int, input().split())
W = str(input().rstrip())
string = str(input().rstrip())

# W의 문자 빈도 수 계산
W_count = {}
for char in W:
    W_count[char] = W_count.get(char, 0) + 1

# 첫번째 윈도우 문자 빈도 수 계산
window_count = {}
for char in string[:g]:
    window_count[char] = window_count.get(char, 0) + 1

answer = 0

# 첫번째 윈도우가 일치하는지 먼저 확인
if window_count == W_count:
    answer += 1

# 두 번째부터 슬라이딩 윈도우
for i in range(g, S):
    # string의 g + 1번째 문자부터 추가
    window_count[string[i]] = window_count.get(string[i], 0) + 1
    # 윈도우의 첫번째 문자 제거
    window_count[string[i - g]] -= 1

    # 빈도가 0일 경우 해당 문자 삭제
    if window_count[string[i - g]] == 0:
        del window_count[string[i - g]]

    # W와 윈도우가 일치하는지 확인
    if window_count == W_count:
        answer += 1

print(answer)