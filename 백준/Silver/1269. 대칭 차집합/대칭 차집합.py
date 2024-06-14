import sys

a, b = map(int, sys.stdin.readline().split())

aArr = list(map(int, sys.stdin.readline().split()))
bArr = list(map(int, sys.stdin.readline().split()))

intrSet = set(set(aArr) & set(bArr))
hapSet = set(set(aArr) | set(bArr))
# print(intrSet)
# print(hapSet)
res = set(hapSet - intrSet)
# print(res)
print(len(res))