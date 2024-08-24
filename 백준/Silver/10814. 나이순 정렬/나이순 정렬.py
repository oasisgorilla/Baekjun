import sys
input = sys.stdin.readline

N = int(input().rstrip())

mems = []

for _ in range(N):
    age, name = input().split()
    mems.append((int(age), name))

mems.sort(key=lambda x: x[0])

for mem in mems:
    print(*mem)