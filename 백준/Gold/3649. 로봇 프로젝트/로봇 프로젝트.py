"""3트"""
import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input().strip()) * int(1e7)
        n = int(input().strip())
        legos = []
        for _ in range(n):
            legos.append(int(input().strip()))

        # 투 포인터 사용을 위한 정렬
        legos.sort()

        # 투 포인터 초기화
        left, right = 0, n - 1
        answer = None

        while left < right:
            total = legos[left] + legos[right]
            if total == x: # left, right가 양 끝에 있을 때 구멍에 들어맞는 경우
                answer = (legos[left], legos[right]) # 가장 차이가 큰 조합이다.
                break
            elif total < x: # 구멍 크기보다 레고 조합이 작은 경우
                left += 1 # 레고 조합의 크기를 키운다
            else: # 구멍 크기보다 레고 조합이 큰 경우
                right -= 1 # 레고 조합의 크기를 줄인다.

        if answer:
            print(f"yes {answer[0]} {answer[1]}")
        else:
            print("danger")
    except Exception:
        break