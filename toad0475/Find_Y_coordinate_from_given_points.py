'''
slope(기울기) = y의 변화량 / x의 변화량
기울기 = y1-y2/x1-x2

y-intercept(y절편)
기울기 * x1 + y절편 = y1
y절편 = y1-(기울기*x1)
'''
def solution(X, points):
    if len(points)<2:
        return -1
    if X < points[0][0] or X > points[-1][1]:
        return -1

    def slope(x1,x2,y1,y2):
        return ((y1 - y2) / (x1 - x2))

    def yintercept(slope,x1,y1):
        return y1-(slope*x1)

    for i in range(len(points)-1):    
        if X >= points[i][0] and X < points[i+1][0]:
            slope = slope(points[i][0],points[i+1][0],points[i][1],points[i+1][1])
            yintercept = yintercept(slope,points[i][0],points[i][1])
            return slope*X+yintercept

# 테스트
print(solution(8,[[0,5],[2,3],[6,2],[10,0]]))
