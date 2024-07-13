import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 명령어의 개수

instruction = []

for i in range(n):
    instruction.append(list(map(str, input().split())))

# instruction operate
stack = [] # stack, stack[-1] is top, stack[0] is bottom

for i in range(n):
    if instruction[i][0] == 'push':
        stack.append(int(instruction[i][1])) # push stuff
    elif instruction[i][0] == 'pop':
        if len(stack) == 0: # empty stack
            print(-1)
        else:
            val = stack.pop()
            print(val)
    elif instruction[i][0] == 'size':
        print(len(stack))

    elif instruction[i][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif instruction[i][0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

