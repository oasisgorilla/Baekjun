import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 월세 내기 바로 전 날, 일을 할 수 있는 날

salarys = list(map(int, input().split()))

cur_sum = sum(salarys[:m])
max_salary = cur_sum

for i in range(1, n - m + 1):
    cur_sum = cur_sum - salarys[i - 1] + salarys[i + m - 1] # 슬라이딩 윈도우 적용
    max_salary = max(max_salary, cur_sum)

print(max_salary)