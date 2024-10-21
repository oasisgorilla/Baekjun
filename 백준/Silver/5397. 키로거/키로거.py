import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip()) # 테스트 케이스 개수

for _ in range(T):
    password = str(input().rstrip()) # 입력한 비밀번호

    stack1 = deque([]) # 커서 앞
    stack2 = deque([]) # 커서 뒤

    for c in password:
        if c == '-':
            if stack1:
                stack1.pop()
            else:
                continue
        elif c == '<':
            if stack1:
                temp = stack1.pop()
                stack2.append(temp)
            else:
                continue
        elif c == '>':
            if stack2:
                temp = stack2.pop()
                stack1.append(temp)
            else:
                continue    
        else:
            stack1.append(c)

    print(''.join(stack1) + ''.join(reversed(stack2)))
