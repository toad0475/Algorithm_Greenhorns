def canJump(nums):
    jump = nums[0]
    if jump >= len(nums)-1: return True, print('True')
    elif jump == 0: return False, print('False')
    else:
        def findallnums(i):
            if i == 0: return [0]
            else: return list(range(1, i+1))
        # 각 아이템들이 가질 수 있는 숫자의 가짓수 찾기
        for i in nums:
            if i == nums[-1]: break
            print(findallnums(i))
        # 각 아이템들의 가짓수를 더한 경우의 수가 nums[-1]보다 같거나 크면 True
        # 아니면 False


canJump([2,0,3,1,1,4])