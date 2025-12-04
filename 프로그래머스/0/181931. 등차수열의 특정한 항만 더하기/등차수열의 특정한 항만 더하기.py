def solution(a, d, included):
    answer = 0
    sequence = a
    for boolean in included:
        if boolean:
            answer += sequence
        sequence += d
    return answer