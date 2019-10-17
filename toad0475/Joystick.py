def solution(name):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = 0
    # 위아래 최소
    for char in name:
        if alphabet.index(char) > 0 and alphabet.index(char) <= 13:
            answer += alphabet.index(char)
        else:
            answer += alphabet.index(char) - ((alphabet.index(char)-13)*2)
    # 양옆 최소?
    for i in range(len(char)):
        if
        
    return answer
