import sys

input = sys.stdin.readline

K = int(input().rstrip())  # 참외 갯수

def find_second(length, idx):
    if len(length) < 2:
        return None
    # 원형 리스트처럼 인덱스를 처리하여 비교
    if length[(idx - 1) % 6] > length[(idx - 5) % 6]:
        return (idx - 1) % 6
    elif length[(idx - 1) % 6] < length[(idx - 5) % 6]:
        return (idx - 5) % 6
    else:
        print("사각형 에러")
        return None

direction = []
length = []

for _ in range(6):
    dire, leng = map(int, input().split())
    direction.append(str(dire))
    length.append(leng)

# first : 제일 긴 변, second : 제일 긴 변과 붙어있는 두번째로 긴 변
first_idx = length.index(max(length))
second_idx = find_second(length, first_idx)

# 전체를 감싸는 사각형에서 안쪽 작은 사각형을 빼서 너비 구하기
big_square = length[first_idx] * length[second_idx]
small_square = length[(first_idx - 3) % 6] * length[(second_idx - 3) % 6]

# 답
answer = (big_square - small_square) * K
print(answer)