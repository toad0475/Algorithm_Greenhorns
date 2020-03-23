from math import gcd
def solution(w, h):
    greatestcommondivisior = gcd(w, h)
    return (w*h)-((w+h)-greatestcommondivisor)

#print(solution(3,3)) #6
#print(solution(8,12)) #80
#print(solution(3,5)) #8
#print(solution(3,4)) #6
#print(solution(5,4)) #6

""" 아래 방법은 4번, 17번 오답, 11, 13,15,16,18번 런타임 오류 
def solution(w,h):
    wh = w*h
    if w == h: return wh * ((w-1)/w)
    else:
        dict = {}
        hbyw = h/w
        wbyh = w/h
        for i in range(1, w):
            dict[i] = hbyw*i
        for i in range(1, h):
            dict[wbyh*i] = i
        
        return wh - (len(dict)+1)
"""
