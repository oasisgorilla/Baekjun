import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())

    candies = list(map(int, input().split()))


    cycle = 0

    for i in range(N): # 처음부터 홀수의 사탕을 가진 경우
        if candies[i] % 2 == 1:
            candies[i] += 1 # 짝수로 보충
    
    if len(set(candies)) == 1: # 첫번째 보충 후 모든 아이가 같은 값을 가져 set 길이가 1이 된 경우
        print(cycle) # 0 출력 후 다음 테스트 케이스로 넘어감
        continue
    
    while True:
        half = [candies[i] // 2 for i in range(N)] # 각 아이들이 보유한 사탕의 1/2 값

        for i in range(N): # 자신의 왼쪽 아이의 1/2 값 + 자신이 보유한 1/2값
            candies[i] = half[i - 1] + half[i]
        
        for i in range(N): # 홀수의 사탕을 가진 아이 사탕 보충
            if candies[i] % 2 == 1:
                candies[i] += 1
        
        cycle += 1 # 위 두 개의 과정을 거치면 사이클 1회 증가

        if len(set(candies)) == 1: # 모든 아이가 같은 값을 가져 set 길이가 1이 된 경우
            break

    print(cycle)



