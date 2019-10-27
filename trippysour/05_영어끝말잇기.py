words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "bot", "tank"]
n = 3
index = 0  # 현재 인덱스 단어
next = index + 1  # 다음 인덱스 단어
for i in words:
    list1 = list(words[index])  # 현재 인덱스 단어를 list1로
    list2 = list(words[next])  # 다음 인덱스 단어를 list2로
    if list1[-1] != list2[0]:  # 현재 리스트 마지막 인덱스 철자가 다음 리스트 첫 인덱스 철자와 다르면
        turn = ((words.index(words[next]) + 1) / n)  # 틀린 문자의 인덱스+1 값을 n으로 나눈 것이 횟수
        who = ((words.index(words[next]) + 1) % n)  # 틀린 문자의 인덱스+1값을 n으로 나눈 몫
        if who == 0: who = who + n  # 만약 몫이 0이라면 마지막 사람이니 n을 더해주고
        else: turn = int((turn + 1))  # 아니라면 turn을 다 못채웠으니 turn에 1을 해주자
        break
    index = index + 1
    next = next + 1
    if index == len(words) - 1:
        break
    else:  # 중복된 단어도 없는데 끝말잇기 까지 잘 했다면 0,0
        who = 0
        turn = 0
if len(words) != len(set(words)):  # words리스트와 words의 set(중복된게 제거 된) len이 다르면
    words.reverse() # words 역순으로 정렬
    for i in words:
        if words.count(words[index]) != 1: # 역순으로 된 리스트들의 요소들의 갯수가 1이 아니라면
            number = len(words) - words.index(words[index]) # 그 인덱스를 words의 len에서 뺴서 원래 words에서 몇번쨰인지 찾기
            turn = number / n  # 틀린 문자의 인덱스값을 n으로 나눈 것이 횟수
            who = number % n  # 틀린 문자의 인덱스값을 n으로 나눈 몫
            if who == 0: who = who + n  # 만약 몫이 0이라면 마지막 사람이니 n을 더해주고
            else: turn = int((turn + 1))  # 아니라면 turn을 다 못채웠으니 turn에 1을 해주자
            break
        index = index + 1
print(who, turn)

# 19번 문제 해결 해야함. 중복이 된 아이템 검사하기, 끝말잇기 잘 했나 둘다 서로 유기적으로 되야함.. 
# 테스트 케이스 n=3 , ["tank", "kick", "know", "wheel", "land", "dream", "mother", "bot", "tank"] 일경우에 "bot"이 틀렸으므로 [2,3]이 나와야하는데 코드상에서 첫번째 tank 검사할 때 마지막 tank가 같다고 [3,3]을 반환
