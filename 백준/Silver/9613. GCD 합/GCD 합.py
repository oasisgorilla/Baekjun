import sys

# 유클리드 호제법
def gcd(a : int, b : int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(sys.stdin.readline().strip()) # 테스트 케이스의 수

# 최대공약수의 합
for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(2, len(arr)):
        for j in range(1, i):
            ans += gcd(arr[i], arr[j])

    print(ans)