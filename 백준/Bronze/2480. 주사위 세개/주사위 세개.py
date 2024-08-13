import sys
input = sys.stdin.readline

dice_value = list(map(int, input().split()))

answer = 0

if dice_value[0] == dice_value[1] == dice_value[2]:
    answer = 10000 + (dice_value[0] * 1000)

elif dice_value[0] != dice_value[1] and dice_value[1] != dice_value[2] and dice_value[0] != dice_value[2]:
    answer = max(dice_value) * 100

else:
    many_value = 0

    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            else:
                if dice_value[i] == dice_value[j]:
                    many_value = dice_value[j]
                    break
                else:
                    continue

    answer = 1000 + (many_value * 100)

print(answer)