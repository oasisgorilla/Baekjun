import sys
input = sys.stdin.readline

R, C = map(int, input().split()) # row, column

string = [input().strip() for _ in range(R)] # 1차원 배열에 문자열 저장

count = 0

columns = ["".join(row[i] for row in string) for i in range(C)] # 열 문자열을 만듦

# 중복 없는 행의 시작점을 이진 탐색으로 찾기
left, right = 0, R - 1

while left <= right:
    mid = (left + right) // 2
    seen = set() # 문자열 중복 체크를 위한 변수
    is_unique = True

    for col in columns: # mid행부터 끝 행까지 확인
        if col[mid:] in seen: # 중복이 있을 경우
            is_unique = False # 체크하고
            break # 탈출
        seen.add(col[mid:]) # seen에 추가
    
    if is_unique:
        left = mid + 1 # 더 많은 행을 제거할 수 있는지 탐색
    else:
        right = mid - 1 # 중복인 행이 없어질 때까지 행을 늘리기
    
print(left - 1)