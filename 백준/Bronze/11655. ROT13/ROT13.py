import sys
input = sys.stdin.readline

string = input().rstrip('\n')

new_string = []

def rot13(char):
    
    curChar = char
    newChar = None

    lowBase = ord('a')
    upBase = ord('A')

    lower = [chr(lowBase + i) for i in range(26)]
    upper = [chr(upBase + i) for i in range(26)]

    if curChar in lower:
        newChar = lower[((ord(curChar) - lowBase) + 13) % 26]
    elif curChar in upper:
        newChar = upper[((ord(curChar) - upBase) + 13) % 26]
    else:
        newChar = char

    return newChar



for i in range(len(string)):
    new_string.append(rot13(string[i]))

print(''.join(new_string))