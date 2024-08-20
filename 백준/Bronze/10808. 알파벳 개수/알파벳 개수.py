import sys

input = sys.stdin.readline

word = list(input().rstrip())

base = ord('a')

answer_list = [0 for _ in range(ord('z') - ord('a') + 1)]

for alphabet in word:
    answer_list[ord(alphabet) - base] += 1

print(*answer_list)