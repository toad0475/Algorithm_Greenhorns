def solution(n):
    if n == 0: return 0
    else:
        answer = []
        for i in range(1, n):
            if n % i == 0: 
                answer.append(n/i)
        return sum(answer)+1
