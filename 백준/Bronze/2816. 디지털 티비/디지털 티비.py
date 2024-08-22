import sys
input = sys.stdin.readline

N = int(input().rstrip())

channel = []

cnt = 0

button = []

for _ in range(N):
    channel.append(input().rstrip())

for i in range(N):
    if channel[i] == 'KBS1':
        break
    else:
        cnt += 1

find1 = ['1' for _ in range(cnt)]
move1 = ['4' for _ in range(cnt)]

button.extend(find1)
button.extend(move1)

cnt = 0

channel.remove('KBS1')
channel.insert(0, 'KBS1')

for i in range(N):
    if channel[i] == 'KBS2':
        break
    else:
        cnt += 1

find2 = ['1' for _ in range(cnt)]
move2 = ['4' for _ in range(cnt - 1)]

button.extend(find2)
button.extend(move2)

print(''.join(button))