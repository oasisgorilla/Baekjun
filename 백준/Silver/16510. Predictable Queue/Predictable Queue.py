import sys
input = sys.stdin.readline

N, M = map(int, input().split())

works = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + works[i - 1]
# print(prefix)
for _ in range(M):
    t = int(input().strip())
    l = 0
    r = N
    while l < r:
        m = (l + r) // 2
        if t > prefix[m]:
            # print(f"l = {l} r = {r} l = m + 1 = {m + 1}")
            l = m + 1
        else:
            # print(f"l = {l} r = {r} r = m = {m}")
            r = m
    if prefix[l] > t:
        l = l - 1
    print(l)