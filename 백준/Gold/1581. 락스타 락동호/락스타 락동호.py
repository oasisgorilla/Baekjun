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