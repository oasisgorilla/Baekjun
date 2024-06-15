import sys

input = sys.stdin.readline

n = int(input().rstrip())
length = len(str(n))
generator = 1

numSum = 0
found = False

while generator < n:
    numSum = 0 # numSum 초기화
    length = len(str(generator)) # 자리수
    for i in range(length):
        numSum += int(str(generator)[i])
    if generator + numSum == n:
        found = True
        break
    generator += 1
    # print(generator)

# print(f"{numSum} + {generator} = {numSum + generator}")
if not found:
    print(0)
else:
    print(generator)