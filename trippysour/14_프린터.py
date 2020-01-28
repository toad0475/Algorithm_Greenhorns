import heapq

def solution(priorities, location):
    answer = 0

    que = [[-v, i] for i, v in enumerate(priorities)]
    heapq.heapify(que)
    
    print(que)
    
    return answer

#print(solution([2,1,3,2], [2])) #1
print(solution([1,1,9,1,1,1], [0])) #5


# max(내림차 순으로) heap 정렬 - i와 i+1이 같지 않다면 순서를 지킴 - 같지 않다면 i-1로부터 가장 작은 차이를 둔 값부터 내보내기 - 다시 max heap 정렬 - 반복?
# 이럴 때 location이 [n][1]과 같다면 그 숫자가 나간 순서...를 반환 

# 우선순위 큐 : https://daimhada.tistory.com/169?category=820522
# 힙큐1 : https://www.daleseo.com/python-heapq/ <-- 여기서 K번째 최대값 찾기 응용? 
# 힙큐2 : https://developer-alle.tistory.com/321
# 큐 : https://www.zerocho.com/category/Algorithm/post/580b9b94108f510015524097
# 힙정렬 : https://gmlwjd9405.github.io/2018/05/10/algorithm-heap-sort.html