array = [2,3,4,5,6,2,3,2]
val = input('element : ')
element = int(val) # 인풋을 int 유형으로 변환
count = array.count(element) # array에서 인풋으로 들어온 숫자가 몇개인지 카운트
for i in range(count): # 카운트 수 만큼 아래 반복
   array.remove(element) # array에서 인풋으로 들어온 숫자 제거
len = len(array) # array의 요소 갯수 구하기
print(len)