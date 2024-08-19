import sys
input = sys.stdin.readline

N = int(input().rstrip())

S = list(input().rstrip())

score = 0

bonus = 0

for i in range(N):
    if S[i] == 'O': # 맞춘 경우
        score += i
        bonus += 1
        score += bonus
    else: # 틀린 경우
        bonus = 0

print(score)
