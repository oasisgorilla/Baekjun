import sys

"""
k년도에서 x를 뺀 값을 M으로 나눈 값이 0이면서 k에서 y를 뺀 값을 N으로 나눈 값도 0이어야 한다.
M이 10, N이 12이고 k가 11인 경우, x는 1, y는 11이 된다.
반대로 계산해보면 딱 들어맞는 것을 알 수 있다.
k - x를 m으로 나눈 값이나 k - y를 n으로 나눈 값, 둘 중 하나를 기준으로 
k를 x나 y로 초기화한 후, m이나 n을 더해주면서 두 조건을 모두 만족시키는 k를 찾아준다.
"""
def solution(m, n, x, y):
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        else:
            k += m
    return -1


t = int(sys.stdin.readline())

for i in range(t):
    input_list = list(map(int,sys.stdin.readline().split()))
    # print(input_list)
    m = input_list[0]
    n = input_list[1]
    x = input_list[2]
    y = input_list[3]
    
    k = solution(m, n, x, y)

    print(k)