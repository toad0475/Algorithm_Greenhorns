import operator
def solution(answers):
    all = [answers, [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    def makelst(n):
        if len(answers) > len(all[n]):
            all[n] = all[n]*int((len(answers)/len(all[n])))
            # 정답이 학생들 답보다 더 길다면 정답에서 학생들의 답수를 나눠서 몫만큼 학생들 답을 곱해주기
            index = 0
            for i in range(len(answers)//len(all[n])):
                # 나머지만큼 append 해서 정답과 같은 리스트로 만들기
                all[n].append(all[n][index])
                index + 1
        return all[n]
    def correct(n):
        index = 0
        count = 0
        for i in range(len(answers)):
            if answers[index] == makelst(n)[index]:
                count = count + 1
            index = index + 1
        return count
    corrects = dict(zip([1,2,3], [correct(1), correct(2), correct(3)]))
    # 1,2,3번째 사람을 Key로 맞춘 값을 value로 딕셔너리 만들기
    sorts = sorted(corrects.items(), key=operator.itemgetter(1), reverse=True)
    # operator를 이용해서 value*itemgetter(1)*를 역순*reverse=true*으로 정렬해서 가장 많이 맞춘 숫자 찾기
    answer = []
    n = 0
    for i in range(len(sorts)):
        if sorts[n][1] == sorts[0][1]:
            # sort[0][1] 값이 sort를 value가 큰 순위로 정리했을 때 제일 큰 값일테니 이것과 비교
            answer.append(sorts[n][0])
        n = n + 1
    return answer

# 위 코드로는 6,10,12,13,14번 틀림
# 런타임 에러가 나는 index 찾기
#def makeindex(n, x):
#    if x > len(all[n]):
#        madeindex = (x % len(all[n]))
#    else:
#        madeindex = x
#    return madeindex
