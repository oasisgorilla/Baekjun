import sys

A, B = map(int, sys.stdin.readline().split())

if A > B:
    A, B = B, A

gcd = 0 # 최대 공약수
lcm = 0 # 최소 공배수

def GCD(a, b):

    while b != 0:
        a, b = b, a%b
    return a

gcd = GCD(A, B)
lcm = A * B // gcd

print(gcd)
print(lcm)