import sys

string = sys.stdin.readline().rstrip() # 커서의 뒷부분

n = int(sys.stdin.readline())

front = list(string) # 커서의 앞부분, 커서는 문자열 맨 뒤에서 시작
back = []

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "L":
        if front:
            back.append(front.pop()) # 커서 앞에서 하나 꺼내서 커서 뒤로 보내준다.
        
    elif command[0] == "D":
        if back:
            front.append(back.pop()) # 커서 뒤에서 하나 꺼내서 앞으로 보내준다.
    
    elif command[0] == "B":
        if front:
            delete = front.pop() # 커서 앞에서 하나 pop

    elif command[0] == "P":
        front.append(command[1]) # 커서 앞에 받은 문자 넣기

res = front + list(reversed(back)) #스택의 top끼리 맞닿아있어야 커서의 움직임이 완성됨

print(''.join(res))
