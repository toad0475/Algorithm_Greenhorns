def solution(n, words):
    index = 0  # 현재 인덱스 단어
    next = index + 1  # 다음 인덱스 단어
    wrong = 0
    wrong1 = 0
    for i in words:
        list1 = list(words[index])  # 현재 인덱스 단어를 list1로
        list2 = list(words[next])  # 다음 인덱스 단어를 list2로
        if list1[-1] != list2[0]:  # 현재 리스트 마지막 인덱스 철자가 다음 리스트 첫 인덱스 철자와 다르면
            wrong = wrong + 1 # 틀린게 있다고 표시
            when1 = words.index(words[next]) + 1
            turn1 = ((words.index(words[next]) + 1) / n)  # 틀린 문자의 인덱스+1 값을 n으로 나눈 것이 횟수
            who1 = ((words.index(words[next]) + 1) % n)  # 틀린 문자의 인덱스+1값을 n으로 나눈 몫
            if who1 == 0: who1 = who1 + n  # 만약 몫이 0이라면 마지막 사람이니 n을 더해주고
            else: turn1 = int((turn1 + 1))  # 아니라면 turn을 다 못채웠으니 turn에 1을 해주자
            break
        index = index + 1
        next = next + 1
        if index == len(words) - 1:
            break     
    index = 0  # 현재 인덱스 단어
    if len(words) != len(set(words)):  # words리스트와 words의 set(중복된게 제거 된) len이 다르면
        wrong1 = wrong1 + 1 # 틀린게 있다고 표시
        words.reverse() # words 역순으로 정렬
        for i in words:
            if words.count(words[index]) != 1: # 역순으로 된 리스트들의 요소들의 갯수가 1이 아니라면
                when2 = len(words) - words.index(words[index]) # 그 인덱스를 words의 len에서 뺴서 원래 words에서 몇번쨰인지 찾기
                turn2 = when2 / n  # 틀린 문자의 인덱스값을 n으로 나눈 것이 횟수
                who2 = when2 % n  # 틀린 문자의 인덱스값을 n으로 나눈 몫
                if who2 == 0: who2 = who2 + n  # 만약 몫이 0이라면 마지막 사람이니 n을 더해주고
                else: turn2 = int((turn2 + 1))  # 아니라면 turn을 다 못채웠으니 turn에 1을 해주자
                break
            index = index + 1
            if index == len(words) - 1:
                break
    if wrong == 0 and wrong1 == 0: # 만약 틀린게 없다면
        who = 0
        turn = 0
    elif wrong != 0 and wrong1 == 0: #만약 첫번째만 틀리면
        who = who1
        turn = turn1
    elif wrong == 0 and wrong1 !=0:
        who = who2
        turn = turn2
    elif wrong != 0 and wrong1 !=0:
        if when1 < when2: # who1의 wrong이 먼저 발생했다면 who1이 who, turn1이 turn
            who = who1
            turn = turn1
        else: # 아니라면 who2, turn2
            who = who2
            turn = turn2
    answer = [who, turn]
    return answer
