from itertools import product
# 두개 이상의 리스트의 모든 조합 구하기 위한 함수 임포트
def canJump(nums):
    if nums[0] >= len(nums)-1: return True, print('True')
    # 첫 인덱스 0의 value가 이미 마지막 인덱스 보다 같거나 크면 True
    elif nums[0] == 0: return False, print('False')
    # 첫인덱스의 value가 0이라면 무조건 False
    else:
        def findallnums(i):
            if i == 0: return [0]
            else: return list(range(1, i+1))
        # 각 아이템들이 가질 수 있는 숫자의 가짓수 찾기
        lst = []
        for i in nums:
            if i == nums[-1]: break
            lst.append(findallnums(i))
            # 그 가짓수들을 2차원 배열에 담기
        print (lst)
        tup = list(product(*lst))
        # 2차원 리스트 들의 조합 가지수 찾기
        print (tup)
        lst2 = []
        i = 0
        for i in tup:
            lst2.append(sum(i))
            if sum(i) >= len(nums)-1: break
        print(lst2)
        if max(lst2) >= len(nums)-1: return True, print(True)
        else: return False, print(False)

        # 각 아이템들의 가짓수를 더한 경우의 수가 len(nums)-1(마지막인덱스)보다 같거나 크면 True
        # 아니면 False


canJump([3,2,1,0,4]) #이거 False 여야함 단순히 더해선 안된다...
