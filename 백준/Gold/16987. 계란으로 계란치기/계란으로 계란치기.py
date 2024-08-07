import sys
input = sys.stdin.readline

N = int(input().rstrip()) # egg count

eggs = []

for _ in range(N):
    S, W = map(int, input().split())
    eggs.append([S, W])

ans = 0

def back(start):
    global ans
    if start == N: # 마지막 계란까지 간 경우
        total = 0 # 깨진 계란 수
        for i in range(N): # 깨진 계란 수 세기
            if eggs[i][0] <= 0: # 내구도가 다 닳은 계란
                total += 1
        
        ans = max(ans, total) # 답 갱신
        return
    
    if eggs[start][0] <= 0: # 지금 들고 있는 계란이 깨진 경우
        back(start + 1)
        return
    
    check = True # 다 깨졌는지 여부(깰 수 있는 계란이 없을 때 고려)
    for i in range(N):
        if i == start: # 들고 있는 계란은 제외
            continue
        if eggs[i][0] > 0: # 하나라도 안깨진 것이 있으면?
            check = False
            break
    
    if check:
        ans = max(ans, N - 1) # 들고 있는 계란 빼고 다 깨진 갯수 갱신
        return
    
    for i in range(N): # 백트래킹
        if i == start or eggs[i][0] <= 0:
            continue
        eggs[start][0] -= eggs[i][1]
        eggs[i][0] -= eggs[start][1]

        back(start + 1)
        # 백트래킹을 하기 위해선 재귀 후 다시 돌려줘야 한다.
        eggs[start][0] += eggs[i][1]
        eggs[i][0] += eggs[start][1]

back(0)

print(ans)