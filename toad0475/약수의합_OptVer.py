# O(n/2)

def solution(n):
    sumdiv = 0
    for i in range(1, (n//2)+1):
        if n%i==0:
            sumdiv += i
    return n + sumdiv
