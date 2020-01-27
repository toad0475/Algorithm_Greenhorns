import math 

def solution(progresses, speeds):
    def remaindays(n1, n2):
        return math.ceil((100 - n1) / n2)

    releases = remaindays(progresses[0], speeds[0]) 
    answer = [0] 
    index = 0 

    for x, y in zip(progresses, speeds):
        print(remaindays(x,y))
        if releases >= remaindays(x,y): 
            answer[index] += 1
        else: 
            releases = remaindays(x,y)
            index += 1
            answer.append(1)

    return answer

#print(solution([0,0,0,0], [100,50,34,25])) #- [1,1,1,1]
#print(solution([93,30,55], [1,30,5])) #- [2,1]
#print(solution([55, 90, 30], [5, 1, 10])) #- [1,2]
#print(solution([5, 5, 5], [21, 25, 20])) #- [3] 
#print(solution([40, 93, 30, 55, 60, 65],  [60, 1, 30, 5 , 10, 7])) #- [1,2,3] 
#print(solution([93, 30, 55, 60, 40, 65],  [1, 30, 5 , 10, 60, 7])) #- [2,4] 
