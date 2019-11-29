nums = [3,2,3]
def majorityElement(nums): 
    return max(set(nums), key = nums.count) 
    # 최대값 = max(iterable, [, default=obj][, key=값을변환할함수])
    # nums 리스트를 set 해서 중복값을 제거 --> 카운트 수로 비교하여 카운트 수가 가장 큰 값을 가진 element를 찾아서 반환
    # 문제 자체가 과반수가 넘는 element가 항상 존재 한다고 하였으므로 과반수가 넘는 수가 max일 수 밖에 없음
print(majorityElement(nums))

# https://leetcode.com/submissions/detail/282448625/
# 176 ms	13.9 MB

#---------------------------------------------------------------------------------------------------------------------
# 아래 코드는 과반수가 넘는 element가 항상 존재 하지 않을 때 통할 듯

def majorityElement2(nums):
    lstset = set(nums)
    lst = list(lstset)
    index = 0
    counts = []
    answer = 0
    for i in range(len(lstset)):
        counts.append(nums.count(lst[index]))
        # Set 한 num의 element들의 카운트를 세서 counts 에 담기
        if counts[index] > len(nums)/2:
            answer = lst[index]
            break
        # 만약 counts의 값이 nums의 과반수가 넘으면 답은 지금 nums의 index 값
        index = index + 1
    return answer
print(majorityElement2(nums))

#https://leetcode.com/submissions/detail/282444993/
# 172 ms	14 MB
