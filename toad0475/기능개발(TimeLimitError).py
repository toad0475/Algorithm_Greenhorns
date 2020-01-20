def solution(progresses, speeds):
    stack=[]
    answer=[]
    while progresses:
        for i in range(len(progresses)):
            if i not in stack:
                if progresses[i]+speeds[i]<100:
                    progresses[i]+=speeds[i]
                else:
                    stack.append(i)
        if stack and stack[-1]==0:
            answer.append(len(stack))
            progresses=progresses[len(stack):]
            speeds=speeds[len(stack):]
            stack.clear()
    return answer
    
print(solution([10,93,30,55,40],[15,1,30,5,20]))
