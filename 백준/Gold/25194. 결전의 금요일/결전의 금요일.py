import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

# %7을 해서 1이 나오면 제자리, (x % 7) - 1 을 해야 함 

dp = [False for _ in range(7)]
dp[0] = True

for work in A:
    temp = [False for _ in range(7)]
    for j in range(7):
        if dp[j]:
            temp[(work + j) % 7] = True
            temp[j] = True
    dp = temp

if dp[4]:
    print("YES")
else:
    print("NO")