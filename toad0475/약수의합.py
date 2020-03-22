def solution(n):
    d = 1
    answer =0
    while d<=n:
        if n%d==0:
            answer += n//d
        d+=1
    return answer
