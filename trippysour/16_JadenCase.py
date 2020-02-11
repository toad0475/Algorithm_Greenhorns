def solution(s):
    answer = []

    lst = s.split(' ')

    for word in lst:
        answer.append(word.capitalize())

    answer = (' '.join(answer))

    return answer
#print(solution('for the last week')) #For The Last Week
#print(solution('3people unFollowed me')) #3people Unfollowed Me
#print(solution("3algOrithm gREENHones   FIGHTING!"))
