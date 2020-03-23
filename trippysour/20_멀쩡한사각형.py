def solution(w,h):
    wh = w*h
    dict = {}
    hbyw = h/w
    wbyh = w/h
    for i in range(1, w):
        dict[i] = hbyw*i
    for i in range(1, h):
        dict[wbyh*i] = i
        
    return wh - (len(dict)+1)

print(solution(3,3)) #6
print(solution(8,12)) #80
print(solution(3,5)) #8
print(solution(3,4)) #6
# 푸는중...
