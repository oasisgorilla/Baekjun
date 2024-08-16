import sys

# 에라토스테네스의 체
primeNum = [False, False] + [True] * 999999 # 0, 1은 소수가 아니다.

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i): # 숫자 i에 대해서
            primeNum[j] = False # i * 2 부터 1000000까지 i의 배수는 소수가 아님

T = int(sys.stdin.readline())

for i in range(T):
    cnt = 0
    N = int(sys.stdin.readline())

    for j in range(2, N // 2 + 1): # 2부터 N//2 + 1까지
        if primeNum[j] and primeNum[N - j]:
            cnt += 1
    print(cnt)