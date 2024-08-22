import sys

input = sys.stdin.readline

A, B = map(int, input().split())
nameA, nameB = input().split()

# A와 B를 합치는 과정
nameAB = []

min_len = min(A, B)

for i in range(min_len):
    nameAB.append(nameA[i])
    nameAB.append(nameB[i])

if A > B:
    nameAB.extend(nameA[min_len:])
else:
    nameAB.extend(nameB[min_len:])

string_list = ''.join(nameAB)

# A와 B를 합친 string_list를 integer_list로 변경하는 과정
base = 65  # 'A'의 아스키 코드
strokes = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
integer_list = [strokes[ord(c) - base] for c in string_list]

# 이름 궁합 산출
while len(integer_list) > 2:
    integer_list = [(integer_list[i - 1] + integer_list[i]) % 10 for i in range(1, len(integer_list))]

# 1의 자리 0 빼고 % 붙여서 출력
if integer_list[0] == 0:
    print(f"{integer_list[1]}%")
else:
    print(f"{integer_list[0]}{integer_list[1]}%")