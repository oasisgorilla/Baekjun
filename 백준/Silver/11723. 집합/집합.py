import sys

m = int(sys.stdin.readline())

s = [0] * 20

for i in range(m):

    instruction = list(map(str, sys.stdin.readline().split()))

  
    if instruction[0] == 'add':
        s[int(instruction[1]) - 1] = 1
    
    elif instruction[0] == 'remove':
        s[int(instruction[1]) - 1] = 0

    elif instruction[0] == 'check':
        print(s[int(instruction[1]) - 1])
    
    elif instruction[0] == 'toggle':
        if s[int(instruction[1]) - 1] == 1:
            s[int(instruction[1]) - 1] = 0
        else:
            s[int(instruction[1]) - 1] = 1
    
    elif instruction[0] == 'all':
        s = [1] * 20

    elif instruction[0] == 'empty':
        s = [0] * 20