import sys
from collections import deque

input = sys.stdin.readline

s = int(input()) # 만들고자 하는 이모티콘 개수
visited = [[0] * 1001 for _ in range(1001)]

###################### bfs ######################

q = deque([[1, 0, 0]]) # 화면의 이모티콘 개수, 클립보드의 이모티콘 개수, 연산 횟수

while q:

    screen, clipboard, cnt = q.popleft()
        
    if screen == s: # 만들고자 하는 이모티콘 개수만큼 화면에 이모티콘이 만들어지면 탈출
        print(cnt)
        break
    
    for i in range(3): # 복사, 붙여넣기, 삭제 3번의 연산

        if i == 0:
            new_clipboard, new_screen = screen, screen # 현재 화면의 이모티콘 클립보드에 복사
        elif i == 1:
            new_screen, new_clipboard = screen + clipboard, clipboard # 현재 클립보드의 이모티콘 화면에 붙여넣기
        else:
            new_screen, new_clipboard = screen - 1, clipboard # 현재 화면의 이모티콘 한 개 빼기
        
        # 만약 새로 계산된 이모티콘과 클립보드의 개수가 범위를 벗어나거나 이미 방문한 적이 있다면 continue
        if new_screen >= 1001 or new_screen < 0 or new_clipboard >= 1001 or new_clipboard < 0 or visited[new_screen][new_clipboard]:
            continue

        # 방문처리 후 연산횟수를 + 1 하여 큐에 추가
        visited[new_screen][new_clipboard] = 1
        q.append([new_screen, new_clipboard, cnt + 1])