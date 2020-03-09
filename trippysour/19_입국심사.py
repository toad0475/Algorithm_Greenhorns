import heapq

def solution(n, times):
    queue = []
    
    for num in times:
        for i in range(1, n):
            heapq.heappush(queue, num * i)
    print(queue)
    for i in range(n):
        answer = heapq.heappop(queue)

    return answer

# print(solution(6, [7, 10])) #answer = 28, queue = [7, 14, 10, 28, 35, 21, 20, 30, 40, 50]
# 1~3번은 통과 4번~9번 타임 리미트로 실패, for문을 많이 써서 그런듯.. 통합해서 n번 이상 안나오게 처리를 해야할 것 같은데..
