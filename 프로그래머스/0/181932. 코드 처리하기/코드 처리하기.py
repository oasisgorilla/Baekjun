def solution(code):
    answer = ''
    mode = False # True = 1, False = 0
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = not mode
            continue
        else:
            if not mode:
                if idx % 2 == 0:
                    answer += code[idx]
            else:
                if idx % 2 == 1:
                    answer += code[idx]
                    
    if len(answer) == 0:
        answer = "EMPTY"
    return answer