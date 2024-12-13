"""2트"""
N, B, W = map(int, input().split())
jem = input().strip()

left = 0
right = 0
b = 0 # 구간 안의 검은돌
w = 0 # 구간 안의 흰돌
max_len = 0

while right < N:
    # 우측으로 확장
    if jem[right] == 'B':
        b += 1
    else:
        w += 1
    right += 1

    while b > B:
        # 좌측 축소
        if jem[left] == 'B':
            b -= 1
        else:
            w -= 1
        left += 1
    
    if w >= W:
        max_len = max(max_len, right - left)

print(max_len)