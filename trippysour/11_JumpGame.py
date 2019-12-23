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
        for i in nums:
            if i == nums[-1]: break
            print(findallnums(i))
        # 각 아이템들의 가짓수를 더한 경우의 수가 len(nums)-1(마지막인덱스)보다 같거나 크면 True
        # 아니면 False


canJump([2,0,3,1,1,4])
