def solution(s):
    s = s.lower()  // 모두 소문자로 만들기
    L=s.split(" ") // split함수를 이용해서 띄어쓰기 단위로 L리스트에 단어를 넣어줍니다
    answer = ""
    for i in L:
        i= i.capitalize() // 단어별로 앞글자만 대문자화해주는 capitalize 함수
        answer+= i+" " // 앞글자만 대문자인 단어를 띄어쓰기를 해서 붙여줍니다
    return answer[:-1] // 글자 마지막에 띄어쓰기가 생기기 때문에 슬라이싱을 해서 글자 마지막 띄어쓰기 이전까지 반환
