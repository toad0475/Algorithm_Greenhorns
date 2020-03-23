def solution(n):
    if n == 0: return 0
    else:
        answer = 0
        for i in range(1, n):
            if n % i == 0: 
                answer += n/i
        return answer + 1
