"""if문만 사용한 풀이(40ms)"""

"""힌트"""

"""
1. 빠르게 시작하는 노래가 한 곡도 없는 경우, 최대 갯수 = SS + min(SF, 1)
2. 빠르게 시작하는 노래는 있지만, 빠르게 시작해서 느리게 끝나는 노래가 한 곡도 없는 경우, 최대 갯수 = FF
3. FS > SF 인 경우, 최대 갯수 = FF + SS + SF * 2 + 1
4. FS <= SF 인 경우, 최대 갯수 = FF + SS + FS * 2 
"""

import sys
input = sys.stdin.readline

song_list = list(map(int, input().split())) # FF, FS, SF, SS

max_song = 0

if song_list[0] > 0 or song_list[1] > 0:
    if song_list[1] == 0: # FF만 존재하는 경우
        max_song = song_list[0]

    else: # FS가 존재하는 경우
        if song_list[1] > song_list[2]: # FS > SF
            max_song = song_list[0] + 1 + song_list[3] + (song_list[2] * 2) # FF 전체 + FS + SS 전체 + SF + FS ... + SF
        else: # FS < SF
            max_song = song_list[0] + song_list[3] + (song_list[1] * 2) # FF 전체 + FS + SS 전체 + SF + FS + ... +SF
else: # FF나 FS가 없는 경우
    max_song = song_list[3] + min(song_list[2], 1)

print(max_song)


"""BFS 사용 풀이(64ms)"""
import sys, collections

# go : kind에 따라 가능한 모든 경우를 탐색하여 최대 가능 공연곡의 수를 리턴하는 함수
def bfs(kind):
    q = collections.deque()
    # check : 현재 곡의 종류가 i, 이때까지 연주한 곡의 수가 j일 때 가능한지 아닌지 체크하는 상태 공간
    check = [[False] * (val + 1) for _ in range(4)]
    # 첫 곡은 항상 가능함
    check[kind][1] = True
    # 종류에 따라 초기값이 달라짐
    if kind == 0:
        q.append((kind, 1, 1, 0, 0, 0))
    elif kind == 1:
        q.append((kind, 1, 0, 1, 0, 0))
    elif kind == 2:
        q.append((kind, 1, 0, 0, 1, 0))
    else:
        q.append((kind, 1, 0, 0, 0, 1))
    while q:
        k, c, ff, fs, sf, ss = q.popleft()
        for i in adj[k]:
             # 더 연주할 수 있고 아직 한번도 가지 않았다면 탐색
            if c + 1 <= val:
                if not check[i][c + 1]:
                    if i == 0 and ff + 1 <= arr[0]:
                        check[i][c + 1] = True
                        q.append((i, c + 1, ff + 1, fs, sf, ss))
                    elif i == 1 and fs + 1 <= arr[1]:
                        check[i][c + 1] = True
                        q.append((i, c + 1, ff, fs + 1, sf, ss))
                    elif i == 2 and sf + 1 <= arr[2]:
                        check[i][c + 1] = True
                        q.append((i, c + 1, ff, fs, sf + 1, ss))
                    elif i == 3 and ss + 1 <= arr[3]:
                        check[i][c + 1] = True
                        q.append((i, c + 1, ff, fs, sf, ss + 1))
                        
    # 가능한 연주곡의 최대값 갱신
    res = 0
    for i in range(4):
        for j in range(val + 1):
            if check[i][j]:
                res = max(res, j)
    return res


arr = list(map(int, sys.stdin.readline().split()))
val = sum(arr)

# adj : 각 곡의 종류에 따라 갈 수 있는 다른 곡의 종류를 저장하는 인접 리스트
adj = [[0, 1], [2, 3], [0, 1], [2, 3]]
ans = 0

# 빠른 시작곡이 있다면 빠른 곡 먼저 연주해야 하므로
if arr[0] > 0:
    ans = max(ans, bfs(0))
if arr[1] > 0:
    ans = max(ans, bfs(1))
# 빠른 시작곡이 없다면 느린 시작곡을 연주할 수 있으므로
if arr[0] == 0 and arr[1] == 0:
    if arr[2] > 0:
        ans = max(ans, bfs(2))
    if arr[3] > 0:
        ans = max(ans, bfs(3))
# 정답 출력
print(ans)
