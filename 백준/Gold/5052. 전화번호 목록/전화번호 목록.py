import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    contacts = []

    is_consistent = True

    for i in range(n):
        contacts.append(input().strip())
    
    contacts.sort()

    for i in range(len(contacts) - 1):
        if contacts[i + 1].startswith(contacts[i]):
            is_consistent = False
            break
    
    if is_consistent:
        print("YES")
    else:
        print("NO")