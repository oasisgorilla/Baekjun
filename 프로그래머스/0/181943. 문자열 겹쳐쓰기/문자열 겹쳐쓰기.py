def solution(my_string, overwrite_string, s):
    answer = ''
    if len(my_string) == len(overwrite_string):
        answer = overwrite_string
    elif s == 0:
        answer = f"{overwrite_string}{my_string[len(overwrite_string):]}"
    elif s == len(my_string) - len(overwrite_string):
        answer = f"{my_string[:len(my_string)-len(overwrite_string)]}{overwrite_string}"
    else:
        answer = f"{my_string[:s]}{overwrite_string}{my_string[s+len(overwrite_string):]}"
    return answer