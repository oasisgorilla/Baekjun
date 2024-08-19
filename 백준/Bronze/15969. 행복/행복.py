import sys
input = sys.stdin.readline

N = int(input().rstrip())

score = list(map(int, input().split()))

diff = max(score) - min(score)

print(diff)