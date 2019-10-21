def solution(name):
    name_list = list(name)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    alphabetinname = []
    alphabetcount = []
    indexcount = []
    realcount = []
    for i in name_list:
        if name_list[index] != 'A': # A가 아닌 element들을 순차적으로 찾음
            alphabetinname.append(name_list[index]) # 찾은 element 들을 alphabetinname에 담음
            indexcount.append(index) # 찾은 element들의 index를 indexcount에  담음
        index = index + 1  # element를 순차적으로 다음 인덱스를 검색하기 위한 + 1
    if len(alphabetinname) > 0: # A가 아닌 element가 0 보다 커야만 아래 수행
        index_alphabet = []
        indexa = 0
        indexb = 0
        indexc = indexb + 1
        for i in alphabetinname:
            index_alphabet = alphabet.index(alphabetinname[indexa])
            if index_alphabet <= len(alphabet) / 2: pass  
            # 만약 alphabet의 갯수의 반인 13 이하라면 alphabet리스트 안에 몇 번 인덱스를 쓰는지 고대로 쓰기
            else: index_alphabet = len(alphabet) - index_alphabet  
            # 아니라면 alphabet의 갯수에서 자신의 인덱스를 빼서 그걸 다시 index_alphabet으로 정의 (Z라면 1이됨, Y는 2)
            alphabetcount.append(index_alphabet)  
            # element마다 나온 값을 alphabetcount라는 리스트에 담기 - 이제 알파벳에 따라 최소 횟수는 찾음
            indexa = indexa + 1
        if len(indexcount) == 1: # 만약에 A가 아닌 알파벳이 하나라면 그 알파벳이 몇번째인지 len의 1/2와 비교한 후 최소 값 찾음
            if indexcount[0] <= len(name_list) / 2:
                count = indexcount[0]
            else:
                count = len(name_list) - indexcount[0]
            answer = sum(alphabetcount) + count
        else:
            for i in indexcount : #indexc가 indexcount의 len를 넘지 않는 한 반복
                if indexcount[indexc] - indexcount[indexb] <= len(name_list) / 2: 
                    # 다음 indexc의 값 - 현재 indexb의 값이 name_list len의 반 이하라면
                    count = indexcount[indexc] - indexcount[indexb] 
                    # 두수 사이에서 가장 빠른 경로로의 차이는 c-b
                else:
                    count = len(name_list) - indexcount[indexc] + indexcount[indexb] 
                    # 아니라면 name_list의 len에서 c의 값을 빼고 뒤로가는 이동도 계산해야하니 b도 더해준다
                realcount.append(count) # 그걸 realcount 안에 담음
                indexb = indexb + 1
                indexc = indexc + 1
                if indexc == len(indexcount):
                    break
            if name_list[0] == 'A': # name의 첫글자가 A라면 
                answer = sum(alphabetcount) + (sum(realcount) + indexcount[0])
                # A가 아닌 리스트인 indexcount의 첫 값을 0 에서 빼서 차이를 구하고 그걸 realcount에서 빼줌)
            else : answer = sum(alphabetcount) + sum(realcount) # 아니라면 그냥 더해주기
    else: answer = 0 # A가 아닌 글자가 하나도 없다면 answer는 0
    return answer
