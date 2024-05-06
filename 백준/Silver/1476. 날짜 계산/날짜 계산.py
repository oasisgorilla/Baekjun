import sys

e, s, m = map(int, sys.stdin.readline().split())

i = 0
j = 0
k = 0

year = 0

while i != e or j != s or k != m:
    if i == 15:
        i = 0
    if j == 28:
        j = 0
    if k == 19:
        k = 0

    i += 1
    j += 1
    k += 1
    year += 1

print(year)