# 리스트로 풀었음

import math
def solution(progresses, speeds):
    remain_list = []
    answer = []
    
    # 남은 일수 계산하여 배열에 셋팅
    remain_list = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    
    # 모든 요소를 실제 배포일로 설정
    for i in range(len(progresses)-1):
        if remain_list[i] > remain_list[i+1]:
            remain_list[i+1] = remain_list[i]
    
    # 배포당일 배포수 추가
    cnt = 1
    for i in range(len(progresses)-1):
        if remain_list[i] >= remain_list[i+1]:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    return answer

print(solution([10,93,30,55,40],[15,1,30,5,20]))
