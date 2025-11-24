str = input()
result = []
for cha in str:
    if cha.islower():
        result.append(cha.upper())
    else:
        result.append(cha.lower())
        
print("".join(result))