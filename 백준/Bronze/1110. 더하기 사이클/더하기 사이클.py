import sys
input = sys.stdin.readline

N = int(input().rstrip())

cnt = 1

num_list = [0, 0]

num_list[0] = N // 10
num_list[1] = N % 10


res = num_list[1] * 10 + (sum(num_list) % 10)

while res != N:

    num_list[0] = res // 10
    num_list[1] = res % 10

    res = num_list[1] * 10 + (sum(num_list) % 10)
    cnt += 1

print(cnt)