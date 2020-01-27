def solution(priorities, location):
    answer = 0
    while location>=0:
        if priorities[0] < max(priorities[1:]):
            priorities.append(priorities.pop(0))
            if location ==0:
                location=len(priorities)-1
                continue
        else:
            priorities.pop(0)
            answer+=1
        location-=1
    return answer