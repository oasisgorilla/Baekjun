import sys

input_arr = list(map(int, sys.stdin.readline().split()))

N = input_arr[0] # 세로 크기
M = input_arr[1] # 가로 크기

arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

max_block = 0

# ㅁㅁㅁㅁ
if M >= 4:
    for i in range(N):
        for j in range(M - 3):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
            if block_sum > max_block:
                max_block = block_sum
    
# ㅁ
# ㅁ
# ㅁ
# ㅁ
for i in range(N - 3):
    for j in range(M):
        block_sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
        if block_sum > max_block:
            max_block = block_sum

# ㅁㅁ
# ㅁㅁ
if M >= 2:
    for i in range(N - 1):
        for j in range(M - 1):
            block_sum = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            if block_sum > max_block:
                max_block = block_sum
            
# ㅁ
# ㅁ
# ㅁㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 2][j + 1]
            if block_sum > max_block:
                max_block = block_sum

#   ㅁ
#   ㅁ
# ㅁㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]
            if block_sum > max_block:
                max_block = block_sum

# ㅁㅁ
#   ㅁ
#   ㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            if block_sum > max_block:
                max_block = block_sum

# ㅁㅁ
# ㅁ
# ㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 2][j]
            if block_sum > max_block:
                max_block = block_sum

# ㅁ
# ㅁㅁㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            if block_sum > max_block:
                max_block = block_sum

#     ㅁ
# ㅁㅁㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            if block_sum > max_block:
                max_block = block_sum

# ㅁㅁㅁ
#     ㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 2]
            if block_sum > max_block:
                max_block = block_sum

# ㅁㅁㅁ
# ㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j]
            if block_sum > max_block:
                max_block = block_sum

# ㅁ
# ㅁㅁ
#   ㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            if block_sum > max_block:
                max_block = block_sum

#   ㅁㅁ
# ㅁㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i + 1][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
            if block_sum > max_block:
                max_block = block_sum

#   ㅁ
# ㅁㅁ
# ㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]
            if block_sum > max_block:
                max_block = block_sum

# ㅁㅁ
#   ㅁㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            if block_sum > max_block:
                max_block = block_sum
# ㅁㅁㅁ
#   ㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1]
            if block_sum > max_block:
                max_block = block_sum

#   ㅁ
# ㅁㅁㅁ
if M >= 3:
    for i in range(N - 1):
        for j in range(M - 2):
            block_sum = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            if block_sum > max_block:
                max_block = block_sum
# ㅁ
# ㅁㅁ
# ㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 1][j + 1]
            if block_sum > max_block:
                max_block = block_sum

#   ㅁ
# ㅁㅁ
#   ㅁ
if M >= 2:
    for i in range(N - 2):
        for j in range(M - 1):
            block_sum = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            if block_sum > max_block:
                max_block = block_sum

print(max_block)