import sys
from collections import deque
input = sys.stdin.readline

string = input().rstrip()

stack = []
queue = deque([])

for i in string:
    stack.append(i)
    queue.append(i)

isPal = True

for i in range(len(string)):
    if stack.pop() != queue.popleft():
        isPal = False
        break
    else:
        continue

if isPal:
    print(1)
else:
    print(0)