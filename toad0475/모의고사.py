def solution(answers):
    answer = []
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    sp1, sp2, sp3 = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == a1[(i%5)]:
            sp1+=1
        if answers[i] == a2[(i%8)]:
            sp2+=1
        if answers[i] == a3[(i%10)]:
            sp3+=1
    answer +=[sp1,sp2,sp3]
    return sorted([ i+1 for i, x in enumerate(answer) if x == max(answer)])
