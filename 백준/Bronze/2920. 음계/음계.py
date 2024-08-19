import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

sequential = True # ascending이나 descending인 경우 True, mixed면 False

if num[0] == 1: # ascending과 mixed 분기
    for i in range(1, len(num)):
        if num[i] < num[i - 1]: # 숫자가 낮아지는 경우
            sequential = False # mixed
            break
        else:
            continue

    if sequential:
        print("ascending")
    else:
        print("mixed")

else: # decending과 mixed 분기
    for i in range(1, len(num)):
        if num[i] > num[i - 1]: #숫자가 상승하는 경우
            sequential = False # mixed
            break
        else:
            continue
    
    if sequential:
        print("descending")
    else:
        print("mixed")



