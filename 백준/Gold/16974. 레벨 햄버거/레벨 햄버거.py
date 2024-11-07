import sys
input = sys.stdin.readline

N, X = map(int, input().split())

dp_layer = [0] * (N + 1) # i-레벨 버거의 레이어
dp_patty = [0] * (N + 1) # i-레벨 버거의 패티 수

dp_layer[0] = 1
dp_patty[0] = 1

# 각 레벨별 버거 레이어, 패티 수 계산
for i in range(1, N + 1):
    dp_layer[i] = 2 * dp_layer[i - 1] + 3 # 빵 + i - 1버거 + 패티 + i - 1버거 + 빵
    dp_patty[i] = 2 * dp_patty[i - 1] + 1 # 위 값에서 빵 2개 뺀 값

def count_patty(layer, x):
    # 0단계 예외처리
    if layer == 0:
        if x > 0:
            return 1
        else:
            return 0
    
    # 햄버거 절반 크기 계산(패티 제외)
    half = (dp_layer[layer] - 1) // 2

    if x == 1:
        return 0
    elif x < half + 1: # 절반보다 적게 먹는 경우
        return count_patty(layer - 1, x - 1) # 빵 1개 x에서 빼주기
    elif x == half + 1: # layer - 1 버거 + 빵 + 패티
        return dp_patty[layer - 1] + 1 # 이전 레이어 버거 + 가운데 패티
    else:
        return dp_patty[layer - 1] + 1 + count_patty(layer - 1, x - dp_patty[layer]) # x에서 먹은 부분 빼주기
    
print(count_patty(N, X))