import sys

n = int(sys.stdin.readline())

cnt = 0
if n < 10:
    cnt += n

if 10 <= n < 100:
    cnt += (n - 9) * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 100 <= n < 1000:
    cnt += (n - 99) * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 1000 <= n < 10000:
    cnt += (n - 999) * 4 # 1000 ~ 9999
    cnt += 900 * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 10000 <= n < 100000:
    cnt += (n - 9999) * 5 # 10000 ~ 99999
    cnt += 9000 * 4 # 1000 ~ 9999
    cnt += 900 * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 100000 <= n < 1000000:
    cnt += (n - 99999) * 6 # 100000 ~ 999999
    cnt += 90000 * 5 # 10000 ~ 99999
    cnt += 9000 * 4 # 1000 ~ 9999
    cnt += 900 * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 1000000 <= n < 10000000:
    cnt += (n - 999999) * 7 # 1000000 ~ 9999999
    cnt += 900000 * 6 # 100000 ~ 999999
    cnt += 90000 * 5 # 10000 ~ 99999
    cnt += 9000 * 4 # 1000 ~ 9999
    cnt += 900 * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 10000000 <= n < 100000000:
    cnt += (n - 9999999) * 8 # 10000000 ~ 99999999
    cnt += 9000000 * 7 # 1000000 ~ 9999999
    cnt += 900000 * 6 # 100000 ~ 999999
    cnt += 90000 * 5 # 10000 ~ 99999
    cnt += 9000 * 4 # 1000 ~ 9999
    cnt += 900 * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

if 100000000 <= n < 1000000000:
    cnt += (n - 99999999) * 9 # 100000000 ~ 999999999
    cnt += 90000000 * 8 # 10000000 ~ 99999999
    cnt += 9000000 * 7 # 1000000 ~ 9999999
    cnt += 900000 * 6 # 100000 ~ 999999
    cnt += 90000 * 5 # 10000 ~ 99999
    cnt += 9000 * 4 # 1000 ~ 9999
    cnt += 900 * 3 # 100 ~ 999
    cnt += 90 * 2 # 10 ~ 99
    cnt += 9 # 1 ~ 9

print(cnt)