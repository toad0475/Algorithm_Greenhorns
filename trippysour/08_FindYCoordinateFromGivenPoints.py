# 주어진 x, y 포인트들(Points)은 좌표 평면에서 서로 직선으로 연결되어 있습니다. 이것을 바탕으로 X 좌표에 상응하는 Y값을 반환하세요.
# ex: x가 8일때 y는 1
x = 0
points = [[0, 5],[2, 3],[6,2],[10,0]]
def usv_attenuation_graph(x, points): # x와 Points 를 입력시 y 값을 return 하는 함수
    index = 0 # for 돌리기 위한 index
    slope = [] # 기울기를 담을 빈 리스트
    x_points = [] # 기울기 코드 돌리기 위한 x 리스트
    y_points = [] # y 리스트
    for i in range(len(points)): # Points의 length의 값 만큼 반복
        x_points.append(points[index][0])
        y_points.append(points[index][1])
        if index + 1 == len(points) : break 
        # 다만 아래부터는 index + 1의 값이 list 너머의 값으로 나올 수 있기에 에러 방지차 len 넘기면 break
        slope.append((points[index + 1][1] - points[index][1]) / (points[index + 1][0] - points[index][0]))
        # 현재 x, y 값과 다음 x, y 값과의 차이를 구해서 y증가량 / x증가량 = 기울기 = slope 에 담기
        index = index + 1
    if x >= points[0][0] and x < points[1][0]: n = 0
    elif x >= points[1][0] and x < points[2][0]: n = 1
    elif x >= points[2][0] and x < points[3][0]: n = 2
    elif x == points[3][0] : n = 3
    # 조건문을 매끄럽게 할 수 있는 방법 알아보자
    y = (x - points[n][0]) * slope[n] + points[n][1]
    # x가 8이라면 y = (8-6)*-0.5 + 2 = -1 + 2 = 1
    # x의 증가량에 y의 증가량의 비율을 구해서 x의 증가량에 대응하는 y의 증가량을 구해서 x가 증가하기 전 값에 대응하는 y가 증가하기 전 값에 더해주기
    return print(y)
usv_attenuation_graph(8 ,points)






