import sys
input = sys.stdin.readline

T = int(input().rstrip()) # 테스트 케이스의 수
for _ in range(T):
    input_list = list(map(int, input().split())) # 등수 a, b
    
    # 2017 상금, 2018 상금
    winner_list = [[(1, 5000000), (2, 3000000), (3, 2000000), (4, 500000), (5, 300000), (6, 100000)], [(1, 5120000), (2, 2560000), (4, 1280000), (8, 640000), (16, 320000)]]


    answer_list = [0, 0]

    for i in range(2):
        part = 0 # 등수별 누적 사람 수
        for j in range(len(winner_list[i])):
            part += winner_list[i][j][0] # 등수를 판별하기 위해 등수별 인원 수 누적
            
            if input_list[i] == 0: # 본선 진출에 못 한 경우
                answer_list[i] = 0
                break

            if input_list[i] <= part: # 해당 등수의 인원 수 안에 들 경우
                answer_list[i] = winner_list[i][j][1] # 상금 책정
                break
            else:
                continue

    print(sum(answer_list))