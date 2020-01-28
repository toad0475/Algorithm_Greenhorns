import math

def solution(progresses, speeds):
    
    def remaindays(n1, n2):
        return math.ceil((100 - n1) / n2)
    
    days = []
    index = 0

    for num in progresses:
        days.append((remaindays(progresses[index], speeds[index])))
        index += 1
    
    index = 0
    release = days[0]
    answer = [0]
    daysindex = 0

    for i in days:
        if release >= days[index]:
            answer[daysindex] += 1
        else:
            release = days[index]
            daysindex += 1
            answer.append(1)
        index += 1
        
    return answer

#print(solution([0,0,0,0], [100,50,34,25])) #- [1,1,1,1]
#print(solution([93,30,55], [1,30,5])) #- [2,1]
#print(solution([55, 90, 30], [5, 1, 10])) #- [1,2]
#print(solution([5, 5, 5], [21, 25, 20])) #- [3] 
#print(solution([40, 93, 30, 55, 60, 65],  [60, 1, 30, 5 , 10, 7])) #- [1,2,3] 
#print(solution([93, 30, 55, 60, 40, 65],  [1, 30, 5 , 10, 60, 7])) #- [2,4] 

#release 가 지금 release보다 크면 release 갱신하고 append, 아니면 원래 있는거에 +1
