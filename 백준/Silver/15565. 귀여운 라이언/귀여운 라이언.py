import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

# 1의 위치를 저장
idxes = [i for i, x in enumerate(dolls) if x == 1]

# 라이언 인형이 K개 이상 존재하지 않으면 -1을 출력하고 종료
if len(idxes) < K:
    print(-1)
else:
    min_length = int(1e9)
    for i in range(len(idxes) - K + 1):
        # K개의 연속된 1을 포함하는 구간 길이 계산
        length = idxes[i + K - 1] - idxes[i] + 1
        min_length = min(min_length, length)
    
    print(min_length)
