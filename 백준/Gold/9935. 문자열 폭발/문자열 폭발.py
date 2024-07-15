import sys
input = sys.stdin.readline

inputString = input().rstrip()

bombString = input().rstrip()

stack = []

for i in range(len(inputString)):
    stack.append(inputString[i])
    if len(stack) >= len(bombString):
        if stack[-len(bombString):] == list(bombString): # 스택의 뒤에서 len(bombString) 번째부터 끝까지 문자배열과 bombString 문자배열과 비교
            for _ in range(len(bombString)):
                stack.pop()
result = ''.join(stack)

print(result if result else "FRULA") # 파이썬식 삼항연산자