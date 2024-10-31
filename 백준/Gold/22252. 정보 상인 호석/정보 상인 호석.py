import sys
import heapq
input = sys.stdin.readline

Q = int(input().rstrip()) # 쿼리 개수

gorillas = {}
total_cost = 0

for _ in range(Q):
    
    data = list(map(str, input().split()))
    opt = int(data[0])
    name = data[1]
    k = int(data[2])
    nums = list(map(int, data[3:]))

    if opt == 1:    
        if name not in gorillas:
            gorillas[name] = []
        
        for num in nums:
            heapq.heappush(gorillas[name], -num) # 음수로 삽입하여 가장 큰 값이 앞에 오게 함
    
    elif opt == 2:
        if name not in gorillas:
            continue

        # 정보 구매
        temp_cost = 0
        try:
            for _ in range(k):
                temp_cost += -heapq.heappop(gorillas[name]) # 음수를 다시 양수로 바꿔준다.
        except:
            pass
        
        total_cost += temp_cost
    
print(total_cost)